export default function Input(props) {

    return(
        <input type={props.type} placeholder={props.placeholderName} onChange={props.onChange}/>
    );
}