set table "Homework_5.pgf-plot.table"; set format "%.5f"
set format "%.7e";; set samples 200; set dummy x; plot [x=-1:1] (-0.03125 + 0.5625*x**2 - 1.11022*10**(-16)*x**3 - 1.5*x**4 - 2.22045*10**(-16)*x**5 + x**6)/720;
