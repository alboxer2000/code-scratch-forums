fetch("./alphabet.json") 
    .then(response => response.json()) 
    .then(data =>
        function() {
                a = data.a
                b = data.b
                c = data.c
                d = data.d
                e = data.e
                f = data.f
                g = data.g
                h = data.h
                i = data.i
                j = data.j
                k = data.k
                l = data.l
                m = data.m
                n = data.n
                o = data.o
                p = data.p
                q = data.q
                r = data.r
                s = data.s
                t = data.t
                u = data.u
                v = data.v 
                w = data.w
                x = data.x
                y = data.y
                z = data.z
                const elem = document.querySelector("#element");
                elem.innerHTML = "<p> + h + e + l + l + o + " " + w + o + r + l + d + "" ";
            });
