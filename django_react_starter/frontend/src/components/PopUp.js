import React, { Component } from "react";
import { Modal, Button } from "react-bootstrap";

export class PopUp extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
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
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
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
