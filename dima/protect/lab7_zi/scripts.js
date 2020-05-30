let times_left = document.getElementById('times-left');

function left(tl) {
    times_left.innerHTML = "Left " + (8 - tl).toString()
}


class User {
    constructor() {
        this.logins = ["Vanya", "Dima", "Sasha"]
        this.passwords = [
            [[1,1],[1,2],[1,3],[2,3],[3,3],[4,3],[5,3],[5,2],[5,1],[3,2],[3,1]],
            [[1,1],[1,2],[1,3],[1,4],[1,5],[2,3],[3,1],[3,2],[3,3],[3,4],[3,5],[4,5],[5,5],[5,4],[5,3],[5,2],[5,1],[4,1]],
            [[9,6],[8,6],[7,6],[7,7],[7,8],[8,8],[9,8],[9,9],[9,10],[8,10],[7,10]]
        ]
    }

    get_user(login) {
        for (let i = 0; i < this.logins.length; ++i) {
            if (this.logins[i] === login) {
                return this.passwords[i]
            }
        }
    }

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
        this.status = 0 // 1 registr | 2 login
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

    check_pass() {
        if (this.old_pass.length !== this.dots.length) {
            return false;
        }
        let c = 0;
        for (let i = 0; i < this.old_pass.length; i++) {
            for (let j = 0; j < this.dots.length; j++) {
                if (this.dots[j][0] === this.old_pass[i][0] && this.dots[j][1] === this.old_pass[i][1]) {
                    c++;
                }
            }
        }
        return c === this.old_pass.length;
    }

    registration(login) {
        view.count = 0
        view.status = 1
        alert("Enter a password")
        left(view.count)
    }

    logging(login) {
        let u = new User()
        view.count = 1
        view.status = 2
        alert("Enter a password " + login)
        left(view.count)
        this.old_pass = u.get_user(login)
    }
}

let view =  new View();

document.getElementById("clear").onclick = function clear() {
    view.clear_window();
};

document.getElementById("singin").onclick = function singin() {
    view.logging(document.getElementById('login').value)
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
    if (view.status === 1) {
        if (view.count === 0) {
            view.old_pass = [];
            for (let i = 0; i < view.dots.length; ++i) {
                view.old_pass[view.old_pass.length] = [view.dots[i][0], view.dots[i][1]]
            }
            view.dots = []
        } else {
            if (!view.check_pass(view.old_pass, view.dots)) {
                alert("Different password! Try again!")
                view.count = 0
            } else {
                if (view.count < 7) {
                } else {
                    alert("Successful")
                }
            }
        }
        view.count++;
        left(view.count)
        view.clear_window()
    } else {
        if (view.count < 7) {
            if (view.check_pass()) {
                alert("Logged in")
            } else {
                alert("Uncorrected password")
                view.count++
            }
        } else {
            alert("Access denied")
        }
        view.dots = []
        left(view.count)
        view.clear_window()
    }
};