function USD_graph(dates) {
    let canvas = document.getElementById('usd_graph');
    let ctx = canvas.getContext('2d');
    ctx.font = '12px Helvetica';
    ctx.fillStyle = 'gray';
    ctx.lineWidth = 0.5;
    ctx.strokeStyle = "gray";
    let step = 25;
    let x_part = 4;
    let y_part = 5;
    ctx.beginPath();

    for (let i = 0; i < 5; ++i){
        ctx.fillText(80 - 5 * i, 5, step + i * step);
        ctx.moveTo(step - 5,step + i * step);
        ctx.lineTo(step + x_part * 90 + 5,step + i * step);
    }

    for (let i = 0; i < dates.length; ++i){
        pos = 90 * x_part / (dates.length - 1);
        ctx.moveTo(step + pos * i,step * 5);
        ctx.lineTo(step + pos * i,step * 5 + 5);
        ctx.fillText(dates[i], step + pos * i - 16, step * 5 + 13);
    }
    ctx.stroke();
}

function EUR_graph(dates) {
    let canvas = document.getElementById('eur_graph');
    let ctx = canvas.getContext('2d');

    ctx.font = '12px Helvetica';
    ctx.fillStyle = 'gray';
    ctx.lineWidth = 0.5;
    ctx.strokeStyle = "gray";
    let step = 25;
    let x_part = 4;
    let y_part = 5;
    ctx.beginPath();

    for (let i = 0; i < 5; ++i){
        ctx.fillText(85 - 5 * i, 5, step + i * step);
        ctx.moveTo(step - 5,step + i * step);
        ctx.lineTo(step + x_part * 90 + 5,step + i * step);
    }

    for (let i = 0; i < dates.length; ++i) {
        pos = 90 * x_part / (dates.length - 1);
        ctx.moveTo(step + pos * i,step * 5);
        ctx.lineTo(step + pos * i,step * 5 + 5);
        ctx.fillText(dates[i], step + pos * i - 16, step * 5 + 13);
    }
    ctx.stroke();
}

function USD_fill(mass) {
    let canvas = document.getElementById('usd_graph');
    let ctx = canvas.getContext('2d');
    ctx.strokeStyle = "#0082ff";
    ctx.lineWidth = 1;
    let step = 25;
    let x_part = 4;
    let y_part = 5;
    ctx.beginPath();
    ctx.moveTo(step,step * 5 - (mass[0] - 60) * y_part);

    for (let i = 1; i < mass.length; ++i) {
        ctx.lineTo(step + x_part * i + 5, step * 5 - (mass[i] - 60) * y_part)
    }
    ctx.stroke();
}

function EUR_fill(mass) {
    let canvas = document.getElementById('eur_graph');
    let ctx = canvas.getContext('2d');
    ctx.strokeStyle = "#0082ff";
    ctx.lineWidth = 1;
    let step = 25;
    let x_part = 4;
    let y_part = 5;
    ctx.beginPath();
    ctx.moveTo(step,step * 5 - (mass[0] - 65) * y_part);

    for (let i = 1; i < mass.length; ++i) {
        ctx.lineTo(step + x_part * i + 5, step * 5 - (mass[i] - 65) * y_part)
    }
    ctx.stroke();
}