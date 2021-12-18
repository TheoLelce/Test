$("#customRange").change(function () {
    // var svg = $("#svg");
    // svg.empty();

    // var new_circle = $("<circle/>").appendTo("#svg");
    var new_circle = $("#circle")

    var val = $(".form-range").val();
    console.log(val)

    switch (val) {
      case "0":
          console.log("ok 0")
          new_circle.attr("fill", "#f16c0e")
          // new_circle.attr({cx : "35", cy : "35", r : "30", fill : "#f16c0e"})
          break;
      case "1":
          console.log("OK 1")
          new_circle.attr("fill", "#f1bb0e")
          break;
      case "2":
          new_circle.attr("fill", "#1fd213")
          break;
      case "3":
          new_circle.attr("fill", "#1381d2")
          break;
      case "4":
          new_circle.attr("fill", "#a713d2")
          break;
      case "5":
          new_circle.attr("fill", "#d21313")
          break;
      case "6":
          new_circle.attr("fill", "#13ccd2")
    }

});