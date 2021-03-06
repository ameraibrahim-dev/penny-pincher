{
    const SEARCH_FIELD_LOCATOR = "#searchField";
    const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
    const TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR = "#total-period-expenses";
    const TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR = "#total-period-earnings";
    let categories = [];

    let options = {
        valueNames: ['name', 'note', 'amount', 'date', {name: 'isExpense', attr: 'value'}],
        page: 10,
        pagination: [{
            name: "pagination",
            paginationClass: "pagination",
            outerWindow: 2,
            innerWindow: 2,
        }],
    };
    $(document).ready(function () {
        $(SEARCH_FIELD_LOCATOR).keyup(function () {
            let val = $(SEARCH_FIELD_LOCATOR).val();
            if (val.length == '') {
                transaction_list.search();
            } else {
                transaction_list.search($(SEARCH_FIELD_LOCATOR).val(), ['note', 'amount', 'date', 'name']);
            }
            //update total
            updateTotal(transaction_list.visibleItems);
        });
        $(DATE_RANGE_FIELD_LOCATOR).change(function () {
            filterFunction();
            //update total
            updateTotal(transaction_list.visibleItems);

        });
        $(document).on("click", "input[type='checkbox']", function () {
            if (categories.includes($(this).attr('id'))) {
                let index = categories.indexOf($(this).attr('id'));
                categories.splice(index, 1);
            }
            readCategories();
            filterFunction();
            updateTotal(transaction_list.visibleItems);
        });
    });
    let transaction_list = new List('transactions-list', options);


    function filterFunction() {
        readCategories();
        let value = $(DATE_RANGE_FIELD_LOCATOR).val();
        start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
        end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));

        transaction_list.filter(function (item) {
            let transact_date = new Date(Date.parse(item.values().date));
            transact_date.setHours(0, 0, 0, 0)
            // console.log(transact_date >= start_date && transact_date <= end_date)
            // console.log(categories.includes(item.values().name))
            if ((transact_date >= start_date && transact_date <= end_date)
                && (categories.includes(removeEncoding(item.values().name)))) {
                return true;
            } else {
                return false;
            }
        });

    }

    function updateTotal(items) {
        let totalPeriodExpenses = 0;
        let totalPeriodEarnings = 0;
        items.forEach(value => {
            if (value.values().isExpense == 'True') {
                totalPeriodExpenses -= parseFloat(value.values().amount.replace(",", ""));
            } else {
                totalPeriodEarnings += parseFloat(value.values().amount.replace(",", ""));
            }
        });
        if (totalPeriodExpenses == 'NaN') {
            totalPeriodExpenses = 0;
        }
        if (totalPeriodEarnings == 'NaN') {
            totalPeriodEarnings = 0;
        }
        // display these total number
        $(TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR).text(Number(totalPeriodExpenses).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));
        $(TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR).text(Number(totalPeriodEarnings).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));

    }

    function readCategories() {
        $.each($("input[type='checkbox']:checked"), function () {
            if (categories.includes($(this).attr('id'))) {

            } else {
                if ($(this).attr('id') == undefined) {

                } else {
                    categories.push($(this).attr('id'));
                }
            }

        });
    }

    function removeEncoding(string) {
        return string.replace(/&Agrave;/g, "??").replace(/&Aacute;/g, "??").replace(/&Acirc;/g, "??").replace(/&Atilde;/g, "??").replace(/&Auml;/g, "??").replace(/&Aring;/g, "??").replace(/&agrave;/g, "??").replace(/&acirc;/g, "??").replace(/&atilde;/g, "??").replace(/&auml;/g, "??").replace(/&aring;/g, "??").replace(/&AElig;/g, "??").replace(/&aelig;/g, "??").replace(/&szlig;/g, "??").replace(/&Ccedil;/g, "??").replace(/&ccedil;/g, "??").replace(/&Egrave;/g, "??").replace(/&Eacute;/g, "??").replace(/&Ecirc;/g, "??").replace(/&Euml;/g, "??").replace(/&egrave;/g, "??").replace(/&eacute;/g, "??").replace(/&ecirc;/g, "??").replace(/&euml;/g, "??").replace(/&#131;/g, "??").replace(/&Igrave;/g, "??").replace(/&Iacute;/g, "??").replace(/&Icirc;/g, "??").replace(/&Iuml;/g, "??").replace(/&igrave;/g, "??").replace(/&iacute;/g, "??").replace(/&icirc;/g, "??").replace(/&iuml;/g, "??").replace(/&Ntilde;/g, "??").replace(/&ntilde;/g, "??").replace(/&Ograve;/g, "??").replace(/&Oacute;/g, "??").replace(/&Ocirc;/g, "??").replace(/&Otilde;/g, "??").replace(/&Ouml;/g, "??").replace(/&ograve;/g, "??").replace(/&oacute;/g, "??").replace(/&ocirc;/g, "??").replace(/&otilde;/g, "??").replace(/&ouml;/g, "??").replace(/&Oslash;/g, "??").replace(/&oslash;/g, "??").replace(/&#140;/g, "??").replace(/&#156;/g, "??").replace(/&#138;/g, "??").replace(/&#154;/g, "??").replace(/&Ugrave;/g, "??").replace(/&Uacute;/g, "??").replace(/&Ucirc;/g, "??").replace(/&Uuml;/g, "??").replace(/&ugrave;/g, "??").replace(/&uacute;/g, "??").replace(/&ucirc;/g, "??").replace(/&uuml;/g, "??").replace(/&#181;/g, "??").replace(/&#215;/g, "??").replace(/&Yacute;/g, "??").replace(/&#159;/g, "??").replace(/&yacute;/g, "??").replace(/&yuml;/g, "??").replace(/&#176;/g, "??").replace(/&#134;/g, "???").replace(/&#135;/g, "???").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&#177;/g, "??").replace(/&#171;/g, "??").replace(/&#187;/g, "??").replace(/&#191;/g, "??").replace(/&#161;/g, "??").replace(/&#183;/g, "??").replace(/&#149;/g, "???").replace(/&#153;/g, "???").replace(/&copy;/g, "??").replace(/&reg;/g, "??").replace(/&#167;/g, "??").replace(/&#182;/g, "??").replace(/&Alpha;/g, "??").replace(/&Beta;/g, "??").replace(/&Gamma;/g, "??").replace(/&Delta;/g, "??").replace(/&Epsilon;/g, "??").replace(/&Zeta;/g, "??").replace(/&Eta;/g, "??").replace(/&Theta;/g, "??").replace(/&Iota;/g, "??").replace(/&Kappa;/g, "??").replace(/&Lambda;/g, "??").replace(/&Mu;/g, "??").replace(/&Nu;/g, "??").replace(/&Xi;/g, "??").replace(/&Omicron;/g, "??").replace(/&Pi;/g, "??").replace(/&Rho;/g, "??").replace(/&Sigma;/g, "??").replace(/&Tau;/g, "??").replace(/&Upsilon;/g, "??").replace(/&Phi;/g, "??").replace(/&Chi;/g, "??").replace(/&Psi;/g, "??").replace(/&Omega;/g, "??").replace(/&alpha;/g, "??").replace(/&beta;/g, "??").replace(/&gamma;/g, "??").replace(/&delta;/g, "??").replace(/&epsilon;/g, "??").replace(/&zeta;/g, "??").replace(/&eta;/g, "??").replace(/&theta;/g, "??").replace(/&iota;/g, "??").replace(/&kappa;/g, "??").replace(/&lambda;/g, "??").replace(/&mu;/g, "??").replace(/&nu;/g, "??").replace(/&xi;/g, "??").replace(/&omicron;/g, "??").replace(/&pi??;/g, "??").replace(/&rho;/g, "??").replace(/&sigmaf;/g, "??").replace(/&sigma;/g, "??").replace(/&tau;/g, "??").replace(/&phi;/g, "??").replace(/&chi;/g, "??").replace(/&psi;/g, "??").replace(/&omega;/g, "??").replace(/&bull;/g, "???").replace(/&hellip;/g, "???").replace(/&prime;/g, "???").replace(/&Prime;/g, "???").replace(/&oline;/g, "???").replace(/&frasl;/g, "???").replace(/&weierp;/g, "???").replace(/&image;/g, "???").replace(/&real;/g, "???").replace(/&trade;/g, "???").replace(/&alefsym;/g, "???").replace(/&larr;/g, "???").replace(/&uarr;/g, "???").replace(/&rarr;/g, "???").replace(/&darr;/g, "???").replace(/&barr;/g, "???").replace(/&crarr;/g, "???").replace(/&lArr;/g, "???").replace(/&uArr;/g, "???").replace(/&rArr;/g, "???").replace(/&dArr;/g, "???").replace(/&hArr;/g, "???").replace(/&forall;/g, "???").replace(/&part;/g, "???").replace(/&exist;/g, "???").replace(/&empty;/g, "???").replace(/&nabla;/g, "???").replace(/&isin;/g, "???").replace(/&notin;/g, "???").replace(/&ni;/g, "???").replace(/&prod;/g, "???").replace(/&sum;/g, "???").replace(/&minus;/g, "???").replace(/&lowast;/g, "???").replace(/&radic;/g, "???").replace(/&prop;/g, "???").replace(/&infin;/g, "???").replace(/&OEig;/g, "??").replace(/&oelig;/g, "??").replace(/&Yuml;/g, "??").replace(/&spades;/g, "???").replace(/&clubs;/g, "???").replace(/&hearts;/g, "???").replace(/&diams;/g, "???").replace(/&thetasym;/g, "??").replace(/&upsih;/g, "??").replace(/&piv;/g, "??").replace(/&Scaron;/g, "??").replace(/&scaron;/g, "??").replace(/&ang;/g, "???").replace(/&and;/g, "???").replace(/&or;/g, "???").replace(/&cap;/g, "???").replace(/&cup;/g, "???").replace(/&int;/g, "???").replace(/&there4;/g, "???").replace(/&sim;/g, "???").replace(/&cong;/g, "???").replace(/&asymp;/g, "???").replace(/&ne;/g, "???").replace(/&equiv;/g, "???").replace(/&le;/g, "???").replace(/&ge;/g, "???").replace(/&sub;/g, "???").replace(/&sup;/g, "???").replace(/&nsub;/g, "???").replace(/&sube;/g, "???").replace(/&supe;/g, "???").replace(/&oplus;/g, "???").replace(/&otimes;/g, "???").replace(/&perp;/g, "???").replace(/&sdot;/g, "???").replace(/&lcell;/g, "???").replace(/&rcell;/g, "???").replace(/&lfloor;/g, "???").replace(/&rfloor;/g, "???").replace(/&lang;/g, "???").replace(/&rang;/g, "???").replace(/&loz;/g, "???").replace(/&#039;/g, "'").replace(/&amp;/g, "&").replace(/&quot;/g, "\"");
    }
}
