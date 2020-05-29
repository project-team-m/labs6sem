// переменная направления
// массив положения змейки
// обработка нажатий кнопок вниз... вниз, то переменная довн
// при просчёте движения змейки case пол довн и тд


class Snake {
    constructor(size) {
        this.positions = [[6, 4], [6, 5], [6, 6]];
        this.deadline = size;
    }

    next_step(new_step) {
        this.positions.shift();
        this.positions[this.length] = new_step;
    }

    get length() {
        return this.positions.length;
    }

    check_inside(mass) {
        for (let i = 0; i < this.length; ++i) {
            if (this.positions[i][0] === mass[0] && this.positions[i][1] === mass[1]) {
                return false;
            }
        }
        return true;
    }

    get death() {
        for (let i = 0; i < this.length; ++i) {
            for (let j = 0; j < this.length; ++j) {
                if (this.positions[i][0] === this.positions[j][0] && this.positions[i][1] === this.positions[j][1] &&
                i !== j) {
                    return false
                }
            }
            if (this.positions[i][0] >= this.deadline ||
                this.positions[i][1] >= this.deadline ||
                this.positions[i][0] < 0 ||
                this.positions[i][1] < 0) {
                return false;
            }
        }
        return true;
    }
}

class View {
    constructor() {
        this.canvas = document.getElementById('c1');
        this.ctx = this.canvas.getContext('2d');
        this.size = 31;
        this.snake = new Snake(this.size);
        this.size_block = 20;
        this.border = 1;
        this.apple_img = new Image();
        this.apple_img.src = 'apple.png';
        this.apple = [-10,10];
        this.old = this.snake.positions[0];
    }

    randomInteger(min, max) {
        // получить случайное число от (min-0.5) до (max+0.5)
        let rand = min - 0.5 + Math.random() * (max - min + 1);
        return Math.round(rand);
    }

    clear_window() {
        this.ctx.clearRect(0, 0, this.size * this.size_block, this.size * this.size_block)
    }

    show_snake() {
        if (this.snake.death){
            this.clear_window();
            this.eat_apple();
            this.ctx.drawImage(this.apple_img, this.apple[0] * this.size_block, this.apple[1] * this.size_block, 20, 20);
            this.ctx.fillStyle = '#080808';
            for (let i = 0; i < this.snake.length - 1; ++i) {
                this.ctx.fillRect(this.snake.positions[i][0] * this.size_block,
                    this.snake.positions[i][1] * this.size_block,
                    this.size_block,
                    this.size_block)
            }

            this.ctx.fillStyle = 'yellow'
            this.ctx.fillRect(this.snake.positions[this.snake.length - 1][0] * this.size_block + this.border,
                this.snake.positions[this.snake.length - 1][1] * this.size_block + this.border,
                this.size_block - this.border,
                this.size_block - this.border)
        } else {
            clearInterval(this.action);
            this.clear_window();
            this.ctx.font = '50px Arial';
            this.ctx.fillStyle = 'red';
            this.ctx.textAlign = "center";
            this.ctx.fillText('YOU DIED',this.canvas.width/2, this.canvas.height/2)
        }

    }

    create_apple() {
        this.apple = [this.randomInteger(0, this.size - 1), this.randomInteger(0, this.size - 1)]
        while (!this.snake.check_inside(this.apple)) {
            this.apple = [this.randomInteger(0, this.size - 1), this.randomInteger(0, this.size - 1)]
        }
        this.ctx.drawImage(this.apple_img, this.apple[0] * this.size_block, this.apple[1] * this.size_block, 20, 20);
    }

    eat_apple() {
        if (!this.snake.check_inside(this.apple)) {
            this.snake.positions.unshift(this.old);
            this.create_apple();
        }
    }

    move() {
        switch (this.way) {
            case 'up':
                this.old = this.snake.positions[0];
                if (this.snake.positions[this.snake.length - 2][1]
                    !== this.snake.positions[this.snake.length - 1][1] - 1) {
                    this.snake.next_step([this.snake.positions[this.snake.length - 1][0],
                        this.snake.positions[this.snake.length - 1][1] - 1]);
                } else {
                    this.way = 'down';
                    this.move()
                }
                break;
            case 'down':
                this.old = this.snake.positions[0];
                if (this.snake.positions[this.snake.length - 2][1]
                    !== this.snake.positions[this.snake.length - 1][1] + 1) {
                    this.snake.next_step([this.snake.positions[this.snake.length - 1][0],
                        this.snake.positions[this.snake.length - 1][1] + 1]);
                } else {
                    this.way = 'up';
                    this.move()
                }
                break;
            case 'left':
                this.old = this.snake.positions[0];
                if (this.snake.positions[this.snake.length - 2][0]
                    !== this.snake.positions[this.snake.length - 1][0] - 1) {
                    this.snake.next_step([this.snake.positions[this.snake.length - 1][0] - 1,
                            this.snake.positions[this.snake.length - 1][1]]);
                } else {
                    this.way = 'right';
                    this.move()
                }
                break;
            case 'right':
                this.old = this.snake.positions[0];
                if (this.snake.positions[this.snake.length - 2][0]
                    !== this.snake.positions[this.snake.length - 1][0] + 1) {
                    this.snake.next_step([this.snake.positions[this.snake.length - 1][0] + 1,
                        this.snake.positions[this.snake.length - 1][1]]);
                } else {
                    this.way = 'left';
                    this.move()
                }
                break;
        }
        this.show_snake();
    }

    key_handler(key) {
        if (key === 'KeyA' && this.save === null && this.way !== 'right') {
            this.way = 'left'
        } else if (key === 'KeyS' && this.save === null && this.way !== 'up') {
            this.way = 'down'
        } else if (key === 'KeyD' && this.save === null && this.way !== 'left') {
            this.way = 'right'
        } else if (key === 'KeyW' && this.save === null && this.way !== 'down') {
            this.way = 'up'
        } else if (key === 'KeyP' && this.save === null) {
            this.save = this.way;
            this.way = 'pause';
        } else if (key === 'KeyP' && this.save !== null) {
            this.way = this.save;
            this.save = null;
        }

    }

    run() {
        this.show_snake();
        this.create_apple();
        this.action = setInterval(() => this.move(), this.sleep);
        document.onkeypress = function(event) {
            view.key_handler(event.code);
        }
    }
}

let view = new View();
view.run();