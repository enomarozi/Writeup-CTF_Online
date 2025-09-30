<h1>Hashing is more secure</h1>
<h3>Description</h3>
<p>https://ringzer0ctf.com/challenges/30</p>
<label>Password</label>
<h3>Solution</h3>
<p>View source page javascript</p>

```javascript
$(".c_submit").click(function(event) {
  event.preventDefault();
  var p = $("#cpass").val();
  if(Sha1.hash(p) == "b89356ff6151527e89c4f3e3d30c8e6586c63962") {
      if(document.location.href.indexOf("?p=") == -1) {   
          document.location = document.location.href + "?p=" + p;
      }
  } else {
      $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
  }
});
```
<label>Password : hash sha1(adminz) = b89356ff6151527e89c4f3e3d30c8e6586c63962</label> 


<h3>Flag</h3>
<pre>
FLAG-bXNsYg9tLCaIX6h1UiQMmMYB
</pre>
