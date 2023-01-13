%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}} </td>
  %end
  <td><button type="submit" name="save" method="GET" onclick="myFunction({{row[0]}})" >Edit</button></td>
  </tr>
%end
</table>
<script>
function myFunction(edit){
    window.location.href="/edit/"+edit;
}
</script>