document.addEventListener("DOMContentLoaded", function() {
  let likeBtn = document.getElementsByClassName("like-btn");
  callOutSection = document.getElementById("callout-text");

  for (let i = 0; i < likeBtn.length; i++) {
    likeBtn[i].addEventListener("click", function(event) {
      if (confirm("Is this working?")) {
        event.preventDefault();
        callOutSection.classList.add("hide-content");
      }
    });
  }
});
