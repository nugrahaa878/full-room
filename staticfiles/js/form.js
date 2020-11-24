export default function validate() {
    let form = document.getElementsByTagName("form");
    let inputs = form.getElementsByTagName('input');

    const emptyInput = inputs.filter(x => x === null)

    console.log(emptyInput);
}