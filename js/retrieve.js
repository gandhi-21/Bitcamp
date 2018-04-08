<script>
function formdata()
{
var firstname1= document.getElementById("Author").value;
var lastname1= document.getElementById("Text").value;
document.writeln("<h1>Confirmation Page</h1><br>");
document.writeln("Thank you for completing this form.<br><br>");
localStorage.setItem('firstname1', JSON.stringify(firstname1));
localStorage.setItem('lastname1', JSON.stringify(lastname1));
}
</script>
