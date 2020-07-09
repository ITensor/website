using ITensors

function ITensors.space(::SiteType"S=3/2";
                        conserve_qns=false)
  if conserve_qns
    return [QN("Sz",3)=>1,QN("Sz",1)=>1,
            QN("Sz",-1)=>1,QN("Sz",-3)=>1]
  end
  return 4
end

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

