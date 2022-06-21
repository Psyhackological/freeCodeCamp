use std::env::{args, Args};

fn main() {
  let mut args: Args = args();

  let first = args.nth(1).unwrap(); // we want 2nd argument
  let operator = args.nth(0).unwrap().chars().next().unwrap(); // we use next, then unwrap it, then we take iterator from strings, and we call next on it which returns a char
  let second = args.nth(0).unwrap(); // then again call next()

  let first_number = first.parse::<f32>().unwrap(); // converting to f32
  let second_number = second.parse::<f32>().unwrap(); // this also
  let result = operate(operator, first_number, second_number);
  let output_string = output(first_number, operator, second_number, result);
  println!("{:?}", output_string);
}

fn operate(operator: char, first_number: f32, second_number: f32) -> f32 {
  match operator {
    '+' => first_number + second_number,
    '-' => first_number - second_number,
    '/' => first_number / second_number,
    '*' | 'x' | 'X' => first_number * second_number,
    _ => panic!("Invalid operator used."),
  }
}

fn output(first_number: f32, operator: char, second_number: f32, result: f32) -> String {
  format!(
    "{} {} {} = {}",
    first_number, operator, second_number, result
  )
}
