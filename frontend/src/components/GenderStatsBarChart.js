import React from "react";
import { Bar } from "@ant-design/charts";
import { connect } from "react-redux";
import { PageHeader} from "antd";

class GenderStatsBarChart extends React.Component {

      render() {
            const config = {
                data: this.props.gender_stats,
                xField: "value",
                yField: "gender",
                seriesField: "gender",
                legend: { position: "top-left" },
            };
            return (
                
                <div>
                      {this.props.gender_stats && (this.props.gender_stats).length>0 &&
                        <div className="site-page-header-ghost-wrapper">
                        <PageHeader
                          title="Total employees population by gender in Chicago, USA"
                        >
                            <Bar {...config} />
                        </PageHeader>
                        </div> 
                      }
                </div>
            );
      }
}

const mapStateToProps = (state) => {
      return state.genderStatsReducer;
};
    
const mapDispatchToProps = (dispatch) => {
      return {};
};
    
export default connect(mapStateToProps, mapDispatchToProps)(GenderStatsBarChart);

