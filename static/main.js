$.get("/api/name/flask").done(response => {
  $("#content")[0].innerHTML += response;
});