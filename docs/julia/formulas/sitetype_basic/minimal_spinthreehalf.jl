using ITensors

ITensors.space(::SiteType"S=3/2") = 4

function ITensors.op!(Op::ITensor,
                      ::OpName"Sz",
                      ::SiteType"S=3/2",
                      s::Index)
  Op[s'=>1,s=>1] = +3/2
  Op[s'=>2,s=>2] = +1/2
  Op[s'=>3,s=>3] = -1/2
  Op[s'=>4,s=>4] = -3/2
end

function ITensors.op!(Op::ITensor,
                      ::OpName"S+",
                      ::SiteType"S=3/2",
                      s::Index)
  Op[s'=>1,s=>2] = sqrt(3)
  Op[s'=>2,s=>3] = 2
  Op[s'=>3,s=>4] = sqrt(3)
end

function ITensors.op!(Op::ITensor,
                      ::OpName"S-",
                      ::SiteType"S=3/2",
                      s::Index)
  Op[s'=>2,s=>1] = sqrt(3)
  Op[s'=>3,s=>2] = 2
  Op[s'=>4,s=>3] = sqrt(3)
end

