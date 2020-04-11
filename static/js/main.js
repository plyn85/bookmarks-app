$(document).ready(function () {
  /* added so flashed messages dissappear after ten seconds */
  setTimeout(function () {
    $("#flashed-message").hide("slow");
  }, 10000);
  // this will hide an show the Instructions text on users category an bookmarks
  $(".info-btn").click(function () {
    $(".user-text").toggle();
  });
});
