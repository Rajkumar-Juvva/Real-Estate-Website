window.addEventListener('DOMContentLoaded', function() {
    // Get the "Possession" field and the "Age of Property" and "Due Date" fields
    var possession = document.getElementById('id_possession');
    var age_of_property = document.getElementsByClassName('field-possession_age')[0];
    var due_date = document.getElementsByClassName('field-possession_due_date')[0];

    // Function to show or hide fields based on "Possession" field value
    function showHideFields() {
        if (possession.value === 'ready_to_move') {
            age_of_property.style.display = 'block';
            due_date.style.display = 'none';
        } else if (possession.value === 'under_construction') {
            age_of_property.style.display = 'none';
            due_date.style.display = 'block';
        } else {
            age_of_property.style.display = 'none';
            due_date.style.display = 'none';
        }
    }

    // Show or hide fields when the "Possession" field value changes
    possession.addEventListener('change', showHideFields);

    // Show or hide fields when the page loads
    window.addEventListener('load', showHideFields);
});
