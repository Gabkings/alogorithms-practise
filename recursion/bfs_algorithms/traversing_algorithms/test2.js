let a = [1, "Turing", { x: 2 },
    [3, 4], { y: 5 }
];

for (let i = 0; i < a.length; i++) {
    if (a[i] === "Turing") a.splice(1.0);
}

console.log(a.length);