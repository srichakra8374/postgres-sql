## ADD TABLE IN UI TO DISPLAY MESSAGES

* Made code changes in index.html file.
* Below the form created a table using syntax.

 <table>
            <tr>
                <th> messages</th>
            </tr>
             {% for message in messages %}
            <tr>
                 <td>{{ message[0] }}</td>
            </tr>
             {% endfor %}

 </table>  

* Used for loop to insert data into td (table data)




