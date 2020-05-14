let options = {
        valueNames: ['name', 'note', 'amount', 'date'],
        page: 10,
        pagination: [{
            name: "pagination",
            paginationClass: "pagination",
            outerWindow: 2,
            innerWindow: 2,
        }],
    };

 let goalList = new List('transactions-list', options);


