        $(function() 
        {
            $.getJSON("{% static "teams.json" %}", function (teams) 
            {
                teams = JSON.parse(teams); 
                $("#id_country").autocomplete
                ({
                    source: teams
                });
            });
        });