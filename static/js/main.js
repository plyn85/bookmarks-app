$(document).ready(function () {
  /* added so flashed messages dissappear after ten seconds */
  setTimeout(function () {
    $("#flashed-message").hide("slow");
  }, 10000);
  // this will hide an show the Instructions text on users category an bookmarks
  $(".info-btn").click(function () {
    $(".user-text").toggle();
  });

//   $(".like-form-btn").on("click", function () {
//     var book_id = $(this).attr("book_id");
//     req = $.ajax({
//       url: "{{url_for('upvote')}}",
//       type: "POST",
//       contentType: "application/json;charset=UTF-8",
//       dataType: "json",
//       data: { id: up_vote_id },
//     });
//   });
// });
