// SLIDERS //
var slider_1 = document.getElementById("chamber_depth_range");
var slider_2 = document.getElementById("minimal_diameter_range");
var slider_3 = document.getElementById("expected_cell_size_px_range");

var output_1 = document.getElementById("chamber_depth");
var output_2 = document.getElementById("minimal_diameter");
var output_3 = document.getElementById("expected_cell_size_px");

output_1.innerHTML = slider_1.value;
output_2.innerHTML = slider_2.value;
output_3.innerHTML = slider_3.value;

slider_1.oninput = function() {
  output_1.innerHTML = this.value;
}
slider_2.oninput = function() {
    output_2.innerHTML = this.value;
  }
  slider_3.oninput = function() {
    output_3.innerHTML = this.value;
  }

// MOUSE CLICKING - COORDINATES//
const canvas = document.getElementById("canvas_mouse_clicking");
const img = document.getElementById("Identified_cells");

let img_size_y = img.height;
let img_size_x = img.width;

coordinates = [];

function getMousePosition(canvas, event) {
  let rect = canvas.getBoundingClientRect();

  canvas.height = rect.height;
  canvas.width = rect.width;

  const context = canvas.getContext("2d");

  let x = (event.clientX - rect.left).toFixed(0); //.toFixed(0) = zero digits
  let y = (event.clientY - rect.top).toFixed(0);

  coordinates.push({x, y});

  identified_cells = coordinates.length;
//
 
  // DRAWING A CIRCLE//
  var circle_size = slider_3.value;

  context.beginPath();
  context.arc(x, y, circle_size, 0, 2*Math.PI, false);  
  context.lineWidth = 1;
  context.strokeStyle = '#FF9900';
  context.stroke();

  // DRAWING ALL CIRCLES//
  for (let i = 0; i < coordinates.length; i++){ 
    context.beginPath();
    context.arc(coordinates[i].x, coordinates[i].y, circle_size, 0, 2*Math.PI, false);  
    context.lineWidth = 1;
    context.strokeStyle = '#FF9900';
    context.stroke();
  }

  document.getElementById("identified_cells").innerHTML = identified_cells;

}

// define mouse click event
canvas.addEventListener("mousedown", function(e){
  getMousePosition(canvas, e);
  });

//-----------------------------//
//--- IMAGES ON FULL SCREEN ---//
//-----------------------------//
$('img[data-enlargeable]').addClass('img-enlargeable').click(function() {
  var src = $(this).attr('src');
  var modal;

  function removeModal() {
    modal.remove();
    $('body').off('keyup.modal-close');
  }
  modal = $('<div>').css({
    background: 'RGBA(0,0,0,.5) url(' + src + ') no-repeat center',
    backgroundSize: 'contain',
    width: '100%',
    height: '100%',
    position: 'fixed',
    zIndex: '10000',
    top: '0',
    left: '0',
    cursor: 'zoom-out'
  }).click(function() {
    removeModal();
  }).appendTo('body');
  //handling ESC
  $('body').on('keyup.modal-close', function(e) {
    if (e.key === 'Escape') {
      removeModal();
    }
  });
});



