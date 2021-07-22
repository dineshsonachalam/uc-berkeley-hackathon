import React from "react";
import { Bar } from "@ant-design/charts";
import { connect } from "react-redux";
import { PageHeader} from "antd";

class RelationshipStatsBarChart extends React.Component {

      render() {
            const config = {
                data: this.props.relationship_stats,
                xField: "value",
                yField: "relationship",
                seriesField: "relationship",
                legend: { position: "top-left" },
            };
            console.log("Config: ", config);
            return (
                
                <div>
                      {this.props.relationship_stats && (this.props.relationship_stats).length>0 &&
                        <div className="site-page-header-ghost-wrapper">
                        <PageHeader
                          title="Relationship status of employees in Chicago, USA"
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
}
    
const mapDispatchToProps = (dispatch) => {
      return {}
}
    
export default connect(mapStateToProps, mapDispatchToProps)(RelationshipStatsBarChart);

