document.addEventListener("DOMContentLoaded", function() {
  likeBtn = document.getElementById("like-btn");
  callOutSection = document.getElementById("callout-text");

  likeBtn.addEventListener("click", function() {
    callOutSection.classList.add("hide-content");
  });
});
