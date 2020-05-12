{
    const NOTE_FIELD_LOCATOR = "#filterByNoteTextField";
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

    let transaction_list = new List('transactions-list', options);
    $(NOTE_FIELD_LOCATOR).keyup(function () {
        let val = $(NOTE_FIELD_LOCATOR).val();
        if (val.length == '') {
            transaction_list.search();
        } else {
            transaction_list.search($(NOTE_FIELD_LOCATOR).val(), ['note']);
        }
        //update total
        updateTotal(transaction_list.visibleItems);


    });
    $(DATE_RANGE_FIELD_LOCATOR).change(function () {
        filterFunction();
        //update total
        updateTotal(transaction_list.visibleItems);

    });

    function isCheckboxChecked() {


        $("input[type='checkbox']").click(function () {
            if (categories.includes($(this).attr('id'))) {

                let index = categories.indexOf($(this).attr('id'));
                categories.splice(index, 1);

            } else {


            }
            //Adds each checked checkbox to array.
            readCategories();
            filterFunction();
            updateTotal(transaction_list.visibleItems);
        });


        return categories;
    }

    function filterFunction() {
        readCategories();
        let value = $(DATE_RANGE_FIELD_LOCATOR).val();
        start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
        end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));

        transaction_list.filter(function (item) {
            let transact_date = new Date(Date.parse(item.values().date));
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
        return string.replace(/&Agrave;/g, "À").replace(/&Aacute;/g, "Á").replace(/&Acirc;/g, "Â").replace(/&Atilde;/g, "Ã").replace(/&Auml;/g, "Ä").replace(/&Aring;/g, "Å").replace(/&agrave;/g, "à").replace(/&acirc;/g, "â").replace(/&atilde;/g, "ã").replace(/&auml;/g, "ä").replace(/&aring;/g, "å").replace(/&AElig;/g, "Æ").replace(/&aelig;/g, "æ").replace(/&szlig;/g, "ß").replace(/&Ccedil;/g, "Ç").replace(/&ccedil;/g, "ç").replace(/&Egrave;/g, "È").replace(/&Eacute;/g, "É").replace(/&Ecirc;/g, "Ê").replace(/&Euml;/g, "Ë").replace(/&egrave;/g, "è").replace(/&eacute;/g, "é").replace(/&ecirc;/g, "ê").replace(/&euml;/g, "ë").replace(/&#131;/g, "ƒ").replace(/&Igrave;/g, "Ì").replace(/&Iacute;/g, "Í").replace(/&Icirc;/g, "Î").replace(/&Iuml;/g, "Ï").replace(/&igrave;/g, "ì").replace(/&iacute;/g, "í").replace(/&icirc;/g, "î").replace(/&iuml;/g, "ï").replace(/&Ntilde;/g, "Ñ").replace(/&ntilde;/g, "ñ").replace(/&Ograve;/g, "Ò").replace(/&Oacute;/g, "Ó").replace(/&Ocirc;/g, "Ô").replace(/&Otilde;/g, "Õ").replace(/&Ouml;/g, "Ö").replace(/&ograve;/g, "ò").replace(/&oacute;/g, "ó").replace(/&ocirc;/g, "ô").replace(/&otilde;/g, "õ").replace(/&ouml;/g, "ö").replace(/&Oslash;/g, "Ø").replace(/&oslash;/g, "ø").replace(/&#140;/g, "Œ").replace(/&#156;/g, "œ").replace(/&#138;/g, "Š").replace(/&#154;/g, "š").replace(/&Ugrave;/g, "Ù").replace(/&Uacute;/g, "Ú").replace(/&Ucirc;/g, "Û").replace(/&Uuml;/g, "Ü").replace(/&ugrave;/g, "ù").replace(/&uacute;/g, "ú").replace(/&ucirc;/g, "û").replace(/&uuml;/g, "ü").replace(/&#181;/g, "µ").replace(/&#215;/g, "×").replace(/&Yacute;/g, "Ý").replace(/&#159;/g, "Ÿ").replace(/&yacute;/g, "ý").replace(/&yuml;/g, "ÿ").replace(/&#176;/g, "°").replace(/&#134;/g, "†").replace(/&#135;/g, "‡").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&#177;/g, "±").replace(/&#171;/g, "«").replace(/&#187;/g, "»").replace(/&#191;/g, "¿").replace(/&#161;/g, "¡").replace(/&#183;/g, "·").replace(/&#149;/g, "•").replace(/&#153;/g, "™").replace(/&copy;/g, "©").replace(/&reg;/g, "®").replace(/&#167;/g, "§").replace(/&#182;/g, "¶").replace(/&Alpha;/g, "Α").replace(/&Beta;/g, "Β").replace(/&Gamma;/g, "Γ").replace(/&Delta;/g, "Δ").replace(/&Epsilon;/g, "Ε").replace(/&Zeta;/g, "Ζ").replace(/&Eta;/g, "Η").replace(/&Theta;/g, "Θ").replace(/&Iota;/g, "Ι").replace(/&Kappa;/g, "Κ").replace(/&Lambda;/g, "Λ").replace(/&Mu;/g, "Μ").replace(/&Nu;/g, "Ν").replace(/&Xi;/g, "Ξ").replace(/&Omicron;/g, "Ο").replace(/&Pi;/g, "Π").replace(/&Rho;/g, "Ρ").replace(/&Sigma;/g, "Σ").replace(/&Tau;/g, "Τ").replace(/&Upsilon;/g, "Υ").replace(/&Phi;/g, "Φ").replace(/&Chi;/g, "Χ").replace(/&Psi;/g, "Ψ").replace(/&Omega;/g, "Ω").replace(/&alpha;/g, "α").replace(/&beta;/g, "β").replace(/&gamma;/g, "γ").replace(/&delta;/g, "δ").replace(/&epsilon;/g, "ε").replace(/&zeta;/g, "ζ").replace(/&eta;/g, "η").replace(/&theta;/g, "θ").replace(/&iota;/g, "ι").replace(/&kappa;/g, "κ").replace(/&lambda;/g, "λ").replace(/&mu;/g, "μ").replace(/&nu;/g, "ν").replace(/&xi;/g, "ξ").replace(/&omicron;/g, "ο").replace(/&piρ;/g, "ρ").replace(/&rho;/g, "ς").replace(/&sigmaf;/g, "ς").replace(/&sigma;/g, "σ").replace(/&tau;/g, "τ").replace(/&phi;/g, "φ").replace(/&chi;/g, "χ").replace(/&psi;/g, "ψ").replace(/&omega;/g, "ω").replace(/&bull;/g, "•").replace(/&hellip;/g, "…").replace(/&prime;/g, "′").replace(/&Prime;/g, "″").replace(/&oline;/g, "‾").replace(/&frasl;/g, "⁄").replace(/&weierp;/g, "℘").replace(/&image;/g, "ℑ").replace(/&real;/g, "ℜ").replace(/&trade;/g, "™").replace(/&alefsym;/g, "ℵ").replace(/&larr;/g, "←").replace(/&uarr;/g, "↑").replace(/&rarr;/g, "→").replace(/&darr;/g, "↓").replace(/&barr;/g, "↔").replace(/&crarr;/g, "↵").replace(/&lArr;/g, "⇐").replace(/&uArr;/g, "⇑").replace(/&rArr;/g, "⇒").replace(/&dArr;/g, "⇓").replace(/&hArr;/g, "⇔").replace(/&forall;/g, "∀").replace(/&part;/g, "∂").replace(/&exist;/g, "∃").replace(/&empty;/g, "∅").replace(/&nabla;/g, "∇").replace(/&isin;/g, "∈").replace(/&notin;/g, "∉").replace(/&ni;/g, "∋").replace(/&prod;/g, "∏").replace(/&sum;/g, "∑").replace(/&minus;/g, "−").replace(/&lowast;/g, "∗").replace(/&radic;/g, "√").replace(/&prop;/g, "∝").replace(/&infin;/g, "∞").replace(/&OEig;/g, "Œ").replace(/&oelig;/g, "œ").replace(/&Yuml;/g, "Ÿ").replace(/&spades;/g, "♠").replace(/&clubs;/g, "♣").replace(/&hearts;/g, "♥").replace(/&diams;/g, "♦").replace(/&thetasym;/g, "ϑ").replace(/&upsih;/g, "ϒ").replace(/&piv;/g, "ϖ").replace(/&Scaron;/g, "Š").replace(/&scaron;/g, "š").replace(/&ang;/g, "∠").replace(/&and;/g, "∧").replace(/&or;/g, "∨").replace(/&cap;/g, "∩").replace(/&cup;/g, "∪").replace(/&int;/g, "∫").replace(/&there4;/g, "∴").replace(/&sim;/g, "∼").replace(/&cong;/g, "≅").replace(/&asymp;/g, "≈").replace(/&ne;/g, "≠").replace(/&equiv;/g, "≡").replace(/&le;/g, "≤").replace(/&ge;/g, "≥").replace(/&sub;/g, "⊂").replace(/&sup;/g, "⊃").replace(/&nsub;/g, "⊄").replace(/&sube;/g, "⊆").replace(/&supe;/g, "⊇").replace(/&oplus;/g, "⊕").replace(/&otimes;/g, "⊗").replace(/&perp;/g, "⊥").replace(/&sdot;/g, "⋅").replace(/&lcell;/g, "⌈").replace(/&rcell;/g, "⌉").replace(/&lfloor;/g, "⌊").replace(/&rfloor;/g, "⌋").replace(/&lang;/g, "⟨").replace(/&rang;/g, "⟩").replace(/&loz;/g, "◊").replace(/&#039;/g, "'").replace(/&amp;/g, "&").replace(/&quot;/g, "\"");
    }
}
