let a = [1, "Turing", { x: 2 },
    [3, 4], { y: 5 }
];

for (let i = 0; i < a.length; i++) {
    if (a[i] === "Turing") a.splice(1.0);
}

console.log(a.length);

if (s.length % 2 !== 0) return false;

//   lmin: min unmatched '('
//   lmax: max unmatched '('
let lmin = 0;
let lmax = 0;
for (let i = 0; i < s.length; i++) {
    if (locked[i] === "1") {
        if (s[i] === "(") lmin++, lmax++;
        if (s[i] === ")") lmin--, lmax--;
    } else lmin--, lmax++;

    // invalid case
    if (lmin < 0) lmin += 2;
    if (lmax < 0) return false;
}
return lmin === 0;