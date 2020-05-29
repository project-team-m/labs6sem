let times_left = document.getElementById('times-left');

function left(tl) {
    times_left.innerHTML = "Left " + (7 - tl).toString()
}

class View {
    constructor() {
        this.canvas = document.getElementById('c1');
        this.ctx = this.canvas.getContext('2d');
        this.size = 11;
        this.size_block = 40;
        this.border = 1;
        this.dots = [];
        this.old_pass = []
        this.count = 0
    }

    clear_window() {
        this.ctx.clearRect(0, 0, this.size * this.size_block, this.size * this.size_block)
        this.dots = [];
    }

    check_not_instance(x, y) {
        for (let i = 0; i < this.dots.length; ++i) {
            if (this.dots[i][0] === x && this.dots[i][1] === y) {
                return false;
            }
        }
        return true;
    }

    fill_pixel(x, y) {
        let x_pos = Math.ceil(x / this.size_block) - 1
        let y_pos = Math.ceil(y / this.size_block) - 1
        if (this.check_not_instance(x_pos, y_pos)) {
            this.dots[this.dots.length] = [x_pos, y_pos];
            this.ctx.fillRect(x_pos * this.size_block,
                y_pos * this.size_block,
                this.size_block,
                this.size_block,)
        }
    }

    check_pass(old_p, new_p) {
        if (old_p.length !== new_p.length) {
            return false;
        }
        let c = 0;
        alert(1) // тут почему то всё зависает паскуда, мать в кино водил
        for (let i = 0; i < old_p.length; i++) {
            for (let j = 0; i < new_p.length; j++) {
                if (new_p[j] === old_p[i]) {
                    c++;
                }
            }
        }
        return c === old_p.length;
    }

    registration(login) {
        view.count = 0
        left(view.count)
    }
}

let view =  new View();

document.getElementById("clear").onclick = function clear() {
    view.clear_window();
};

document.getElementById("singin").onclick = function singin() {
    let a = 1;
};

document.getElementById("singup").onclick = function singup() {
    view.registration(document.getElementById('login').value)
};

view.canvas.onmousemove = function drawIfPressed (e) {
    if (e.buttons > 0) {
        view.fill_pixel(e.offsetX, e.offsetY)
    }
};

document.getElementById("confirm").onclick = function confirm() {
    left(view.count)
    if (view.count === 0) {
        view.old_pass = [];
        for (let i = 0; i < view.dots.length; ++i) {
            view.old_pass[view.old_pass.length] = [view.dots[i][0], view.dots[i][1]]
        }
        view.dots = []
    } else {
        if (view.check_pass(view.old_pass, view.dots) !== true) {
            alert("Different password! Try again!")
            view.count = 1
        } else {
            if (view.count < 7) {
            } else {
                alert("Successful")
            }
        }
    }
    view.count++;
    view.clear_window()
};