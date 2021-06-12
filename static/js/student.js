let array = [
    [
        "Ram",
        "21",
        "Male",
    ],
    [
        "Mohan",
        "32",
        "Male",
    ],
    [
        "Rani",
        "42",
        "Female",
    ],
    [
        "Johan",
        "23",
        "Female",
    ],
    [
        "Shajia",
        "39",
        "Female",
    ]
];

$(document).ready(function() {
    $('#result').DataTable({
        data: array,
        "pageLength": 3,
        "scrollX": true
    });
} );