window.onload = function() {
  setInterval(function() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", location.pathname);
      xhr.setRequestHeader("Pragma", "no-cache");
      xhr.setRequestHeader("Cache-Control", "no-cache");
      xhr.setRequestHeader("If-Modified-Since", new Date(document.lastModified).toUTCString());
      xhr.onreadystatechange  = function (e) {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            location.reload();
          }
        }
      };
      xhr.send();
  }, 1000);
};
