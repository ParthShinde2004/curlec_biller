import React, { Component } from "react";
import { Modal, Button } from "react-bootstrap";

export class PopUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      companies: [],
    };
  }

  state = {
    loading: true,
    companies: null,
  };

  async componentDidMount() {
    const url = "http://127.0.0.1:8000/api/showcalculations";
    const response = await fetch(url);
    const data = await response.json();
    // this.setState({ companies: data.data.company_name, loading: false });
    this.setState({ companies: data.Map(d)})
    console.log(data.data);
  }

  render() {
    // console.log(JSON.stringify(CalcData));
    // for (let i = 0; i < 5; i++) {
    //   console.log(CalcData["data"][i]["company_name"]);
    // }
    // console.log(CalcData["data"].length);
    return (
      console.log(this.state.companies)
      <Modal
        {...this.props}
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header className="bg-primary">
          <Modal.Title id="contained-modal-title-vcenter" className="text-info">
            Calculation Rules Settings
          </Modal.Title>
          <button
            type="button"
            className="close"
            data-dismiss="modal"
            onClick={this.props.onHide}
          >
            <span aria-hidden="true" className="modal_button">
              &times;
            </span>
            <span className="sr-only">Close</span>
          </button>
        </Modal.Header>
        <Modal.Body>
          <h6>Customer</h6>
          <select className="form-control" aria-label=".form-select-sm example">
            <option defaultValue>Select Customer</option>
            <option value="1">One</option>
            <option value="2">Two</option>
          </select>

          <h6>Calculation Rule - Credit Card:</h6>
          <div className="input-group">
            {this.state.loading || !this.state.companies ? (
              <div>loading...</div>
            ) : (
              <div>
                <div>{this.state.companies}</div>
              </div>
            )}
          </div>
          <h6>Calculation Rule - CASA:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>
          <h6>Calculation Rule - Instant Pay:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>
          <h6>Calculation Rule - Monthly Dashboard Fee:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>
          <h6>Calculation Rule - Monthly Credit Card Fee:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>
          <h6>Calculation Rule - Monthly Mandate Fee:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>
          <h6>Calculation Rule - Mandate Fee:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>
          <h6>Discount Rate - Credit Card:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div>
          <h6>Is Live</h6>
          <select className="form-control" aria-label=".form-select-sm example">
            <option defaultValue>Yes</option>
            <option value="1">No</option>
          </select>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={this.props.onHide}>Save</Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default PopUp;
