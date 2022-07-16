
# use this file to write rust code
# write the rust code in the string argument

python3 -m run_rust '

// This is just an example
// feel free to edit the rust code here

fn main() {
    let sum: i32 = add(4, 5);
    println!("Sum of 4 + 5 is: {sum}");
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}

'

