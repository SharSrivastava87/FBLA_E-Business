"""    <button type="button" id="add-booking-btn" class="text-center" >Add new booking+</button>
    <script>
        var formNum = 1;
        var addButton = document.getElementById('add-booking-btn');
        var form = document.getElementById('availability-form');

        addButton.addEventListener('click', function() {
            // Clone the form
            var newForm = form.cloneNode(true);

            // Update the form's ID and clear its values
            newForm.id = 'availability-form-' + formNum;
            var inputs = newForm.getElementsByTagName('input');
            for (var i = 0; i < inputs.length; i++) {
                inputs[i].value = '';
            }

            // Add the new form after the existing form
            form.parentNode.insertBefore(newForm, form.nextSibling);

            // Increment the form number for the next form
            formNum++;
        });
    </script>"""