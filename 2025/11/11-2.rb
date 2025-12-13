# typed: strict
require 'sorbet-runtime'
extend T::Sig

sig { params(filename: String).returns(T::Hash[String, T::Array[String]]) }
def get_data(filename)
    lines = File.readlines filename
    lines.filter! { |line| line != "" }

    rules = T::Hash[String, T::Array[String]].new
    lines.each do |line| 
        variable, expansions = line.split(":")
        if !variable || !expansions
            raise "file error"
        else
            rules[variable] = expansions.split(" ")
        end
    end
    rules
end

class Node
    extend T::Sig

    sig { params(name: String).void }
    def initialize(name)
        @name = name
        @children = T.let(Array.new, T::Array[Node])
        @parents = T.let(Array.new, T::Array[Node])
        @number = T.let(0, Integer)
    end

    sig { returns(String) }
    attr_reader :name

    sig { returns(T::Array[Node]) }
    attr_accessor :children

    sig { returns(T::Array[Node]) }
    attr_accessor :parents

    sig { returns(Integer) }
    attr_accessor :number
end

sig { params(rules: T::Hash[String, T::Array[String]], start_device: String, end_device: String).returns(Integer) }
def count_paths(rules, start_device, end_device)
    # build graph
    nodes = T.let(Hash.new { |hash, key| hash[key] = Node.new(key) }, T::Hash[String, Node])
    rules.each do |var, expansions|
        expansions.each do |expansion|
            var_node = nodes[var]
            expansion_node = nodes[expansion]
            raise "error" unless var_node and expansion_node
            var_node.children.append(expansion_node)
            expansion_node.parents.append(var_node)
        end
    end

    root = T.let(nil, T.nilable(Node))
    leaf = T.let(nil, T.nilable(Node))
    nodes.each do |name, node| 
        if node.parents.length == 0
            root = node
        elsif node.children.length == 0
            leaf = node
        end
    end

    # give each node a number for the maximum number of steps from root
    ptrs = T::Set[Node].new()
    ptrs.add(T.must(root))
    steps = 0
    while ptrs.length > 0 do
        next_ptrs = T::Set[Node].new()
        ptrs.each do |node|
            node.number = steps
            node.children.each do |node| 
                next_ptrs.add(node)
            end
        end
        steps += 1
        ptrs = next_ptrs
    end
    
    start_node = T.must(nodes[start_device])
    end_node = T.must(nodes[end_device])

    # make pointers at start and end, and traverse until they meet

    down_ptrs = T::Hash[Node, Integer].new()
    down_ptrs[start_node] = 1

    up_ptrs = T::Hash[Node, Integer].new()
    up_ptrs[end_node] = 1

    totalCount = 0
    while down_ptrs.length > 0 or up_ptrs.length > 0 do
        new_down_ptrs = T::Hash[Node, Integer].new()
        new_up_ptrs = T::Hash[Node, Integer].new()

        # want to avoid being stung by e.g.
        # a─►b─►c─►d
        # │        ▲
        # └────────┘
        # so just process the pointers with the lowest .number (steps from root) value
        # (when going down, and highest when going up)
        min_down_number = down_ptrs.length == 0 ? 0 : T.must(down_ptrs.min_by { |node, c| node.number })[0].number
        max_up_number = up_ptrs.length == 0 ? 0 : T.must(up_ptrs.max_by { |node, c| node.number })[0].number

        down_ptrs.filter { |ptr, downCount| ptr.number > min_down_number }.each do |ptr, downCount|
            new_down_ptrs[ptr] = downCount
        end

        down_ptrs.filter { |ptr, downCount| ptr.number == min_down_number }.each do |ptr, downCount|
            ptr.children.each do |node|
                if up_ptrs.include?(node)
                    upCount = T.must(up_ptrs[node])
                    totalCount += downCount * upCount
                elsif node.number > end_node.number
                    # doesn't actually speed up noticeably, but seems correct
                    next
                elsif new_down_ptrs.include?(node)
                    new_down_ptrs[node] = T.must(new_down_ptrs[node]) + downCount
                else
                    new_down_ptrs[node] = downCount
                end
            end
        end

        up_ptrs.filter { |ptr, upCount| ptr.number < max_up_number }.each do |ptr, upCount|
            new_up_ptrs[ptr] = upCount
        end

        up_ptrs.filter { |ptr, upCount| ptr.number == max_up_number }.each do |ptr, upCount|
            ptr.parents.each do |node|
                if new_down_ptrs.include?(node)
                    downCount = T.must(new_down_ptrs[node])
                    totalCount += downCount * upCount
                elsif node.number < start_node.number
                    next
                elsif new_up_ptrs.include?(node)
                    new_up_ptrs[node] = T.must(new_up_ptrs[node]) + upCount
                else
                    new_up_ptrs[node] = upCount
                end
            end
        end

        up_ptrs = new_up_ptrs
        down_ptrs = new_down_ptrs
    end
    totalCount
end

sig {params(rules: T::Hash[String, T::Array[String]]).void}
def outputAsGraphviz(rules)
    rules.each_with_index do |(var, expansions), index|
        expansions.each do |expansion|
            puts "#{var} -> #{expansion};"
        end
    end
end

filename = "11.txt"
rules = get_data(filename)

puts count_paths(rules, "svr", "fft")  * count_paths(rules, "fft", "dac") * count_paths(rules, "dac", "out")
