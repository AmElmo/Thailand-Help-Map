

const displayData = (data) => {
  console.log(data);
}

  const fetchMapData = async () => {
    const result = await fetch('http://thailandhelpmap.com/covid_volunteers.json', {mode: 'no-cors'});
    return await result.json();
  }






//   const data = await fetchMapData();
//   displayData(data);
//   dataset = data
//   console.log(dataset)
// ();


// var json2 = "Yeahhh"

// function fetchurl(){
// fetch("http://localhost:8010/proxy/covid_volunteers.json")
//     .then(function(resp){
//         return resp.json();})
//     .then(function(json){
//         newFunction(json);
//     });
// }

// fetchurl();

// function newFunction(json) {
//     json2 = json
//     console.log(json2);
// }

// console.log(json2)



// var data = fetchjson()
// fetchjson();
// console.log(fetchjson())

/* 

var data = [{"name": "Alice","number": 10},
   {"name": "Bob","number": 20},
   {"name": "Mary","number": 50}];

var newData = data.map(function(d){ return d.number});
console.log(newData);


/* Read JSON file
const fs = require('fs');

let rawdata = fs.readFileSync('covid_volunteers.json');
let student = JSON.parse(rawdata);
console.log(student)

-----

const { JSDOM } = require( "jsdom" );
const { window } = new JSDOM( "" );
const $ = require( "jquery" )( window );

console.log("Hi")

$.getJSON("http://127.0.0.1:8081/covid_volunteers.jsoncallback=?", function(json) {
    console.log(JSON.stringify(json));
});

----

const fetch = require("node-fetch");


    fetch('http://localhost/covid_volunteers.json')
        .then(res => res.json())
        .then(data => {
        console.log(data);
    })

    ---

    var getJSON = require('get-json')

var json2 = getJSON('http://127.0.0.1:8081/covid_volunteers.json', function(error, json){
 
    console.log(json);
});


*/