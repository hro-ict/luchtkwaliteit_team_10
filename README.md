
##  Example send request to endpoint (back-end)

```javascript

const server_data= {
    //max 5 days
    //year-month-day
    start_date: "2023-10-10",
    end_date: "2023-10-15"
}
$.ajax({
  type: "POST",
  url: "http://143.47.183.218:3389/get_data",
  data: JSON.stringify(server_data),
  contentType: "application/json",
  dataType: 'json' ,
  success: function(data){
    //data 5 days predictions
    console.log(data)
  },
  error: function(err){
    console.log(err)
  }
});

```

## Example response
```json
{
  "data": [
    {
      "date": "2023-10-10", 
      "hour": "0:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "1:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "2:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "3:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "4:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "5:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "6:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "7:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "8:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "9:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "10:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "11:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "12:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "13:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "14:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "15:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "16:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "17:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "18:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "19:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "20:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "21:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "22:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-10", 
      "hour": "23:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "0:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "1:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "2:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "3:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "4:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "5:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "6:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "7:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "8:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "9:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "10:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "11:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "12:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "13:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "14:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "15:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "16:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "17:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "18:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "19:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "20:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "21:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "22:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-11", 
      "hour": "23:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "0:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "1:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "2:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "3:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "4:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "5:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "6:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "7:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "8:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "9:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "10:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "11:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "12:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "13:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "14:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "15:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "16:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "17:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "18:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "19:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "20:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "21:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "22:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-12", 
      "hour": "23:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "0:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "1:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "2:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "3:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "4:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "5:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "6:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "7:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "8:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "9:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "10:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "11:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "12:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "13:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "14:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "15:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "16:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "17:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "18:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "19:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "20:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "21:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "22:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-13", 
      "hour": "23:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "0:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "1:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "2:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "3:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "4:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "5:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "6:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "7:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "8:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "9:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "10:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "11:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "12:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "13:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "14:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "15:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "16:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "17:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "18:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "19:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "20:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "21:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "22:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-14", 
      "hour": "23:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "0:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "1:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "2:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "3:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "4:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "5:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "6:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "7:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "8:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "9:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "10:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "11:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "12:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "13:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "14:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "15:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "16:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "17:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "18:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "19:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "20:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "21:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "22:00", 
      "state": "GOED"
    }, 
    {
      "date": "2023-10-15", 
      "hour": "23:00", 
      "state": "GOED"
    }
  ]
}

