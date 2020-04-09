$(document).ready(function () {
  /* added so flashed messages dissappear after ten seconds */
  setTimeout(function () {
    $("#flashed-message").hide("slow");
  }, 10000);

  // overriding default on like the like button here
  $(".like-btn-form").click(function (event) {
    event.preventDefault();
    // run flask route here
    window.location = location.href;
  });

  // this will hide an show the Instructions text on users category an bookmarks
  $(".info-btn").click(function () {
    $(".user-text").toggle();
  });
});

// p_limit = int(request.args.get('limit', 6))
// p_offset = int(request.args.get('offset', 0))
//   "current_url": f"/index?limit={str(p_limit)}&offset={str(p_offset = p_limit)}"
