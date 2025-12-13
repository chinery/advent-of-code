# typed: strict
require 'sorbet-runtime'
extend T::Sig

sig { params(filename: String).returns(T::Hash[String, T::Array[String]]) }
def getdata(filename)
    lines = File.readlines filename
    lines.filter! { |line| line != "" }

    rules = T::Hash[String, T::Array[String]].new
    lines.each do |line| 
        variable, expansions = line.split(":")
        if !variable or !expansions
            raise "file error"
        else
            rules[variable] = expansions.split(" ")
        end
    end
    rules
end

filename = "11.txt"
rules = getdata filename

paths = T::Array[T::Array[String]].new
paths.append ["you"]

donepaths = T::Array[T::Array[String]].new
while paths.length > 0 do
  nextpaths = []
  paths.each do |path|
    last_device = path.last
    raise "error" unless last_device

    expansions = rules[last_device]
    raise "error" unless expansions

    expansions.each do |expansion|
        if expansion == "out"
            donepaths.append path + [expansion]
        else
            nextpaths.append path + [expansion]
        end
    end
  end
  paths = nextpaths
end

puts donepaths.length