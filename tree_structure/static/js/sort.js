var page_num = 1;
var sort_text = 'date_added';
var search_text_all = '';
window.onkeyup = keyup;

function num_up() {
    page_num = page_num + 1;
    sort();
};

function num_down() {
    page_num = page_num - 1;
    sort();
};

function search_text(i) {
    if (i === undefined) {
        sort_text = 'date_added';
    } else {
        sort_text = i;
    }
    sort();
};

function keyup(e) {
    search_text_all = e.target.value;
    sort();
};

function sort() {
    $.ajax(
    {
        type:"GET",
        url:"/employees_all",
        data:{sort_by: sort_text,
            page: page_num,
            q_search: search_text_all,
        },

        success : function (data) {
            $("#div_sort").replaceWith(data);
        }
    })
};
