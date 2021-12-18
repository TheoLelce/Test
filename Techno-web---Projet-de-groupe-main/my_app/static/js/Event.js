
var movement = 0
function Display_Event(){
    $.ajax({
        url: '/get_event',
        type: 'GET',
        dataType: "json",
        async: false,
        success: function(data) {
            event=data
        }
    });

    $.ajax({
        url: '/get_user',
        type: 'GET',
        dataType: "json",
        async: false,
        success: function(data) {
            user=data
        }
    });
    event.sort(function(a,b){return a.getTime() - b.getTime()});
    var EventList = document.getElementById('EventList');
    EventList.innerHTML = "";   
    //Create the table and colomn
    var today = new Date();
    var days =(today.getDay());
    const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
    todayname = (0 - today.getDay());
    for (var i = todayname; i < todayname+7; i++ ){
        var today = new Date();
        var days  = (today.getDay()+i);
        today.setDate(today.getDate() + i + movement);
        var date = today.getDate()+'-'+ (today.getMonth()+1) +'-'+today.getFullYear();
        var table = document.createElement("table");
        var tr = document.createElement("tr");
        var th = document.createElement("th"); 
        th.appendChild(document.createTextNode(` |${weekday[days]} - ${date}`));
        tr.appendChild(th);
        table.appendChild(tr);
        for(i=0;i<event.length;i++){
                if (date = event[i].start_hour && event[i].user_id == user.id){
                tr = document.createElement("tr");
                var td = document.createElement("td");
                td.appendChild(document.createTextNode( i+ e)); //(description)
                tr.appendChild(td);
                table.appendChild(tr);
                }
            }
        EventList.appendChild(table);
    }
    var table = document.createElement("table");
    var tr = document.createElement("tr");
    var th = document.createElement("th");
    td = document.createElement("td");
    button = document.createElement('button');
    button.innerHTML="last";
    button.setAttribute('onclick', 'last();');
    td.appendChild(button);
    tr.appendChild(td);
    td = document.createElement("td");
    button = document.createElement('button');
    button.innerHTML="now";
    button.setAttribute('onclick', 'now();');
    td.appendChild(button);
    tr.appendChild(td);
    td = document.createElement("td");
    button = document.createElement('button');
    button.innerHTML="next";
    button.setAttribute('onclick', 'next();');
    td.appendChild(button);
    tr.appendChild(td);
    table.appendChild(tr);

    EventList.appendChild(table);
}

// add a new task 

function next(){
    movement= movement+7;
    Display_Event();
}

function last(){
    movement= movement-7;
    Display_Event();
}

function now(){
    movement= 0;
    Display_Event();
}
