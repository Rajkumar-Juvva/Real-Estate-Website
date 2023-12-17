window.addEventListener('DOMContentLoaded', function() {
    // Get the "Possession" field and the "Age of Property" and "Due Date" fields
    var possession_1 = document.getElementById('id_possession_0');
    var possession_2 = document.getElementById('id_possession_1');
    var age_of_property = document.getElementsByClassName('field-possession_age')[0];
    var due_date = document.getElementsByClassName('field-possession_due_date')[0];

    // Function to show or hide fields based on "Possession" field value
    function age_of_property_event(){
        if (possession_1.checked){
            age_of_property.style.display = 'block';
        }
        else{
            age_of_property.style.display = 'none';
        }
    }
    function due_date_event(){
        if (possession_2.checked){
            due_date.style.display = 'block';
        }
        else{
            due_date.style.display = 'none';
        }
    }

    // Show or hide fields when the "Possession" field value changes
    possession_1.addEventListener('change', age_of_property_event);
    possession_2.addEventListener('change', due_date_event);

    // Show or hide fields when the page loads
    window.addEventListener('load', age_of_property_event);
    window.addEventListener('load', due_date_event);
});
