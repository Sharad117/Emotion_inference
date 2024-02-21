/* 
JavaScript file for the voltmeter with static data
- Contains functions for drawing the voltmeter using HTML5 Canvas
- Uses static data instead of fetching from a JSON file
*/

(function () {
    "use strict";
}());

var voltage = 24.5,
    targetVoltage = 24.5,
    decrement = null,
    job = null;

// Main entry point for drawing the voltmeter
function draw() {
    var canvas = document.getElementById('voltmeter'),
        options = null;

    // Canvas good?
    if (canvas !== null && canvas.getContext) {
        options = buildOptionsAsJSON(canvas, voltage);

        // Clear canvas
        clearCanvas(options);

        // Draw the metallic styled edge
        drawMetallicArc(options);

        // Draw thw background
        drawBackground(options);

        // Draw ticks
        drawTicks(options);

        // Draw labels on markers
        drawTextMarkers(options);

        // Draw voltmeter color arc
        drawVoltmeterColourArc(options);

        // Draw the needle and base
        drawNeedle(options);
    } else {
        alert("Canvas not supported by your browser!");
    }

    // Check if the current voltage is equal to the target voltage
    if (targetVoltage == voltage) {
        clearTimeout(job);
        return;
    } else if (targetVoltage < voltage) {
        decrement = true;
    } else if (targetVoltage > voltage) {
        decrement = false;
    }

    // Update the current voltage based on the target voltage
    if (decrement) {
        if (voltage - 0.1 < targetVoltage)
            voltage = voltage - 0.01;
        else
            voltage = voltage - 0.05;
    } else {
        if (voltage + 0.1 > targetVoltage)
            voltage = voltage + 0.01;
        else
            voltage = voltage + 0.05;
    }

    // Schedule the next draw
    job = setTimeout(draw, 5);
}

// Manually start the drawing process
draw();
