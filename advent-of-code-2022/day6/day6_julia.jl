text=read("day6.txt", String)

### PART 1
function id(text,n_marker)
    i=1
    while i < length(text) -n_marker -1
        marker=text[i:i+(n_marker-1)]
        if length(Set(marker)) == n_marker
            break
        end
        i+=1
    end
    i+=n_marker-1
end

n_marker=4
println(id(text,n_marker))

### PART 2 : only n_marker is changed
n_marker=14
println(id(text,n_marker))
