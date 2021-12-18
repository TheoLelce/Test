/**
* Displays the user's lessons in the calendar
*/
function displayLessons(){

    $.ajax({
        url: '/get_lessons',
        type: 'GET',
        dataType: "json",
        async: false,
        success: function(data) {
            lessons=data
        }
    });

    $.ajax({
        url: '/get_user',
        type: 'GET',
        dataType: "json",
        async: false,
        success: function(data) {
            user=data
            current_year=$("#filter").val()
        }
    });
    $('td.cell').text("");
    for(i=0;i<lessons.length;i++){
        if(lessons[i].years == current_year && lessons[i].studies == user.studies){
            document.getElementById(lessons[i].jour+'-'+lessons[i].start_hour).textContent = lessons[i].title
        }
    }
}


/**
* JQuery functions
*/
$(document).ready(function(){
    displayLessons()

});


