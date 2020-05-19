{
    let options = {
        valueNames: [{name: 'wallet-type', attr: 'data-attr-wallet-name'},'wallet-type'],
        page: 6,
        pagination: [{
            name: "pagination",
            paginationClass: "pagination",
            outerWindow: 2,
            innerWindow: 2,
        }],
    };
     let wallet_list = new List('wallet-list', options);
}