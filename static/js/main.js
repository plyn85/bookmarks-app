let likeBtnForm = document.getElementsByClassName("like-btn-from");

for (let i = 0; i < likeBtnForm.length; i++) {
  likeBtnForm[i].addEventListener("submit", function (event) {
    event.preventDefault();
  });
}

$(document).ready(function () {
  /* added so flashed messages dissappear after ten seconds */
  setTimeout(function () {
    $("#flashed-message").hide("slow");
  }, 10000);
  // this will hide an show the Instructions text on users category an bookmarks page
  $(".info-btn").click(function () {
    $(".user-text").toggle();
  });
});
