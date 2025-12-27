struct Region
  width::Int
  height::Int
  target::Vector{Int}
end

function Region(s::AbstractString)
    parts = split(s)
    dims  = split(parts[1], 'x')

    width  = parse(Int, dims[1])
    height = parse(Int, dims[2][1:end-1])
    shapes = parse.(Int, parts[2:end])

    Region(width, height, shapes)
end

function getinput(filename::AbstractString)
  nextshape = falses(3,3)
  i = 1

  shapes = Vector{BitMatrix}()
  regions = Vector{Region}()

  open(filename) do f
    for line in readlines(f)
      if length(line) == 0
        # empty line follows shape def
        push!(shapes, copy(nextshape))
        i = 1
      elseif occursin(r"^\d+:$", line)
        # a shape index, can ignore
        continue
      elseif occursin(r"^[#\.]+$", line)
        # part of a shape def
        nextshape[i, :] = collect(line) .== '#'
        i += 1
      elseif occursin(r"^\d+x\d+", line)
        # a region def
        push!(regions, Region(line))
      else
        throw("parse error")
      end
    end
  end

  shapes, regions
end

function main()
  filename = "12.txt"
  shapes, regions = getinput(filename)

  shapesum = sum.(shapes)
  shapesize = prod(size(shapes[1]))

  count = 0
  for i in range(1, stop=size(regions, 1))
    presents = regions[i].target
    minsize = sum(presents .* shapesum)
    maxsize = sum(presents .* shapesize)

    availablesize = regions[i].width * regions[i].height

    if maxsize <= availablesize
      count += 1
    elseif minsize > availablesize
      # don't count
    else
      # TODO: solve NP Hard problem
      @assert false
    end
  end

  println(count)
end

main()