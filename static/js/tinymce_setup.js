tinymce.init({
                    selector: "textarea",
                    plugins: [
                            "advlist autolink lists link image charmap print preview anchor",
                        "searchreplace visualblocks code fullscreen",
                        "insertdatetime media table contextmenu paste "
                        ],
                    toolbar: "insertfile undo redo | styleselect fontsizeselect sizeselect| bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
                    autosave_ask_before_unload: false,
                    image_dimensions: false,
                    extended_valid_elements:"script[language|type|src]",
                    min_height: 160,
                    height : 230
                    });
