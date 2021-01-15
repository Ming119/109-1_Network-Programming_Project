function validate() {
    var ddl = document.getElementById("start");
    var selectedValue = ddl.options[ddl.selectedIndex].value;
    if (selectedValue == "null") {
        alert("請選擇車站");
    }

    var ddl = document.getElementById("end");
    var selectedValue = ddl.options[ddl.selectedIndex].value;
    if (selectedValue == "null") {
        alert("請選擇車站");
    }
}
