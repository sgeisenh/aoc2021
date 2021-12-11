function readall(filename)
    local fh = assert(io.open(filename, "rb"))
    local contents = assert(fh:read("*a"))
    fh:close()
    return contents
end

function split(str, sep)
    local t, ll
    t = {}
    ll = 0
    if (#str == 1) then
        return {str}
    end
    while true do
        l = string.find(str, sep, ll, true)
        if l ~= nil then
            table.insert(t, string.sub(str, ll, l - 1))
            ll = l + 1
        else
            table.insert(t, string.sub(str, ll))
            break
        end
    end
    return t
end

function map(tbl, f)
    local t = {}
    for k, v in pairs(tbl) do
        t[k] = f(v)
    end
    return t
end
