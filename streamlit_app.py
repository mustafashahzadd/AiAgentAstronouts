import streamlit as st
import groq
import os
import random
from dotenv import load_dotenv  


env_path = os.path.join("groq_env", ".env")
load_dotenv(env_path)  # Load environment variables from groq_env/.env

# Retrieve API Key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Initialize Groq Client
groq_client = groq.Groq(api_key=GROQ_API_KEY)

# Sidebar Dropdown Selection
st.sidebar.title("🚀 Select a Mission Module")
option = st.sidebar.selectbox(
    "Which module do you want to use?",
    [
        "Mission Planner",
        "Resource Optimizer",
        "Communication Manager",
        "Supply Chain Manager"
    ]
)

# ----------------------------------- ADD "NEED HELP?" SECTION HERE -----------------------------------
with st.sidebar.expander("💡 Need Help? Click to Expand"):
    help_option = st.selectbox(
        "📖 Select a module to learn more:",
        ["Mission Planner", "Resource Optimizer", "Communication Manager", "Supply Chain Manager"]
    )

    if help_option == "Mission Planner":
        st.markdown("""
        ## 🪐 **Mission Planner Guide**  
        **Plan your mission by selecting essential details.**  
        
        - **🌌 Mission Name:** Choose a unique mission name (e.g., *Artemis II* or *Voyager X*).  
        - **👩‍🚀 Crew Size:** Specify the number of astronauts for the mission. Minimum: 1, Maximum: 10.  
        - **🪐 Destination:** Select a planetary body (Mars, Europa, Titan, etc.).  
        - **🤖 AI Assistant:** Enable this option to include an AI co-pilot for decision-making.  
        - **📏 Distance Calculation:** The system automatically calculates the **estimated travel time** based on spacecraft speed and distance.  
        - **🗓️ Mission Duration:** AI suggests a mission duration between **6 to 36 months** based on the selected destination.  
        """)

    elif help_option == "Resource Optimizer":
        st.markdown("""
        ## 🔋 **Resource Optimizer Guide**  
        **Efficiently allocate power, fuel, and mission-critical equipment.**  

        - **🔌 Power Usage (kW):** Enter the estimated power consumption for mission equipment and systems.  
          - Example: **500 kW** for large satellites, **250 kW** for a rover, **100 kW** for a small module.  
        - **⛽ Fuel Usage (liters):** Fuel required based on mission duration and propulsion type.  
          - Example: **200 liters** for a short-range mission, **1000 liters** for a deep-space probe.  
        - **🛠️ Equipment Details:** List the critical mission hardware.  
          - Example: **Solar Panels, Propulsion Engines, Life Support Systems, Antennas.**  
        - **📊 Optimization:** AI balances energy consumption and suggests adjustments to **maximize efficiency**.  
        """)

    elif help_option == "Communication Manager":
        st.markdown("""
        ## 📡 **Communication Manager Guide**  
        **Ensure stable data transmission and real-time communication with ground control.**  

        - **📶 Signal Strength (dB):** Measures how strong the communication signal is.  
          - Example: **50 dB** = strong, **30 dB** = weak, may need amplification.  
        - **⏳ Latency (ms):** Time delay in sending/receiving messages between spacecraft and ground.  
          - Example: **200 ms** for good connection, **500+ ms** for high delay (may cause issues in real-time control).  
        - **🚨 Message Priority:** Assign importance to messages.  
          - Options: **Routine, Critical, Emergency.**  
          - Example: **Emergency alerts** (life support failure) are prioritized over **Routine logs**.  
        - **⚠️ Data Error Rate (%):** The percentage of errors in data transmission.  
          - Example: **1%** = minimal data loss, **10%+** = severe interference.  
        - **📍 Routing Strategy:** AI suggests **best ground stations and backup connections** based on the above parameters.  
        """)

    elif help_option == "Supply Chain Manager":
        st.markdown("""
        ## 📦 **Supply Chain Manager Guide**  
        **Optimize inventory, supplier lead times, and logistics for mission success.**  

        ### **📋 Inventory Management**  
        - **🔧 Sensors:** Number of high-resolution sensors required.  
          - Example: **150 units** for environmental monitoring.  
        - **📡 Communication Systems:** Enter the required satellite communication modules.  
          - Example: **100 units** for deep-space signals.  
        - **🔋 Solar Panels:** Power generation units for spacecraft.  
          - Example: **250 panels** for long-duration missions.  

        ### **🚀 Propulsion & Fuel System**  
        - **🌀 Ion Thrusters:** Number of electric propulsion engines.  
          - Example: **50 thrusters** for interplanetary travel.  
        - **🚀 Chemical Rockets:** High-power fuel-based engines for acceleration.  
          - Example: **30 rockets** for landing/takeoff.  

        ### **🕗 Lead Time Calculation**  
        - **⏳ Sensors Lead Time:** Expected delivery time for sensors.  
          - Example: **20 days** from supplier.  
        - **📡 Communication Systems Lead Time:**  
          - Example: **15 days** from the manufacturer.  
        - **🔋 Solar Panels Lead Time:**  
          - Example: **25 days** (custom-made components).  

        ### **🚛 Logistics & Transportation**  
        - **🚢 Transportation Modes:** Choose between **Air Freight, Sea Shipping, Ground Transport.**  
          - AI selects the **fastest & most cost-efficient** method based on **distance and urgency.**  
        """)

# -------------------------------------- END OF "NEED HELP?" SECTION --------------------------------------

# Display Mission Title & Introduction
st.markdown(
    """
    <h1 style='text-align: center; font-size: 50px;'>
        🚀 LaunchReady AI:<br> Your Ultimate Mission Guide
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h3 style='text-align: center;'>
        This AI-powered assistant helps astronauts fully prepare for space missions by optimizing resources, 
        managing communication, and planning logistics.
    </h3>
    """,
    unsafe_allow_html=True
)



# Show description for each module
if option == "Mission Planner":
    st.markdown("📌 **Mission Planner**: Helps define objectives, schedules, and risk management for space missions.")
elif option == "Resource Optimizer":
    st.markdown("📌 **Resource Optimizer**: Optimizes power, fuel, and equipment allocation for efficiency.")
elif option == "Communication Manager":
    st.markdown("📌 **Communication Manager**: Manages data transmission, signal strength, and network stability.")
elif option == "Supply Chain Manager":
    st.markdown("📌 **Supply Chain Manager**: Ensures efficient inventory and logistics for space operations.")
elif option == "All Modules":
    st.markdown("📌 **All Modules**: A full suite integrating all space mission components.")

# --------------------------------------------- Run Resource Optimizer only if selected-----------------------------------------------------
if option == "Resource Optimizer":
    st.subheader("🚀 AI Resource Optimization & Efficiency Agent")

    # User Inputs with structured suggestions
    power = st.text_input("🔋 Power Usage (in kW)", placeholder="Enter estimated power consumption")
    st.caption("Example: **500 kW** for a large satellite, **250 kW** for a rover, **100 kW** for a small module.")

    fuel = st.text_input("⛽ Fuel Usage (in liters)", placeholder="Enter fuel consumption per mission")
    st.caption("Example: **200 liters** for a small mission, **1000 liters** for a heavy rocket, **500 liters** for a space station.")

    equipment = st.text_area("🛠️ Equipment Details", placeholder="List key equipment used in the mission")
    st.caption("Example: **Solar panels, Propulsion engines, Life support systems, Communication relay**.")

    # Help Button
    if st.button("💡 Need Help?"):
        st.markdown("""
        **🔋 Power Usage:** Amount of electrical power consumed during the mission.  
        **⛽ Fuel Usage:** Quantity of fuel required for propulsion and mission operations.  
        **🛠️ Equipment Details:** Critical tools and machinery used, which impact efficiency and resource allocation.
        """)

    # AI Agent Class
    class AIAgent:
        def __init__(self, role, task):
            self.role = role
            self.task = task

        def generate_response(self, input_text):
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": f"You are a {self.role}. Your task is: {self.task}"},
                        {"role": "user", "content": input_text}
                    ],
                    temperature=0.7,
                    max_tokens=2000,
                )
                return response.choices[0].message.content if response.choices else "No response received."
            except Exception as e:
                return f"Error: {e}"

    # Define AI Agents
    resource_optimizer = AIAgent(
        role="Smart Resource Allocation Agent",
        task="""Analyze power, fuel, and equipment inputs to optimize mission resources efficiently. 
        - Prioritize **optimal energy distribution** while minimizing fuel dependency.
        - If solar panels are available, consider **solar panel efficiency (~20%)** and **energy storage losses (2% per cycle)**.
        - Provide a **structured breakdown** of power and fuel allocation in **tabular format**.
        - Remove unnecessary headings and focus on relevant calculations.
        - Ensure the response includes a clear, **quantitative analysis**.

        ### **Resource Allocation Summary**
        | Parameter         | Value |
        |------------------|-------|
        | Total Power Required | {power_input} kW |
        | Fuel Available  | {fuel_input} liters |
        | Equipment Used  | {equipment_input} |

        ### **Optimized Power and Fuel Breakdown**
        | Source          | Power Contribution (kW) | Efficiency Factor | Adjusted Output (kW) |
        |---------------|----------------------|-----------------|--------------------|
        | Solar Panels  | Based on input efficiency | 20% | Calculated Output |
        | Fuel-Based Power | Remaining requirement | Fuel efficiency rate | Required Fuel Usage |

        ### **Optimization Strategy**
        - Adjust power consumption to balance energy production and minimize fuel waste.
        - Optimize solar power deployment and introduce hybrid power storage.
        """
    )

    inefficiency_detector = AIAgent(
        role="Waste & Fuel Optimization Agent",
        task="""Detect inefficiencies in power, fuel, and equipment usage, and suggest improvements. 
        - Identify **fuel wastage** and suggest reduction strategies.
        - Detect **power mismanagement** and propose efficiency improvements.
        - Analyze **equipment utilization** and recommend better deployment or energy-saving strategies.
        - Instead of listing inefficiencies as paragraphs, present them in a **structured table**.
        
        ### **Inefficiency Detection & Fixes**
        | Issue              | Identified Cause                          | Suggested Fix |
        |-------------------|--------------------------------------|--------------|
        | Fuel Wastage      | High fuel consumption despite solar use | Optimize combustion system |
        | Power Mismanagement | Uneven energy distribution            | Upgrade power management system |
        | Equipment Inefficiency | Poor solar panel placement          | Improve orientation |

        ### **Final Optimization Strategy**
        - **Reduce fuel reliance** by improving solar panel efficiency.
        - **Introduce energy storage** to balance power fluctuations.
        - **Monitor real-time efficiency metrics** and adjust fuel flow dynamically.
        """
    )

    # Initialize session state for optimization & inefficiency results
    if "optimization_result" not in st.session_state:
        st.session_state.optimization_result = None
    if "inefficiency_result" not in st.session_state:
        st.session_state.inefficiency_result = None

    # Button to Execute Optimization
    if st.button("🔍 Optimize Resources"):
        if power and fuel and equipment:
            st.subheader("✅ Smart Resource Optimization:")
            st.session_state.optimization_result = resource_optimizer.generate_response(
                f"Optimize resource usage for a space mission with {power} kW power, {fuel} liters fuel, "
                f"and the following equipment: {equipment}."
            )
            st.write(st.session_state.optimization_result)
        else:
            st.warning("Please enter all resource details before optimization.")

    # Show inefficiency button only after optimization, without removing optimized results
    if st.session_state.optimization_result:
        if st.button("⚠️ Check for Inefficiencies"):
            st.subheader("⚠️ Inefficiency Detection & Improvement Suggestions:")
            st.session_state.inefficiency_result = inefficiency_detector.generate_response(
                f"Analyze inefficiencies in a space mission using {power} kW power, {fuel} liters fuel, "
                f"and the following equipment: {equipment}."
            )

    # Display inefficiency result without removing optimization result
    if st.session_state.inefficiency_result:
        st.write(st.session_state.inefficiency_result)

#----------------------------------------Supply Chain Manager code here--------------------------
elif option == "Supply Chain Manager":
    st.subheader("🚀 AI Supply Chain Management Agent")

    # User Inputs for Inventory Details
    st.markdown("### 📦 Enter Supply Chain Details for Optimization")
    sensors_inventory = st.number_input("🔧 Sensors", min_value=0, placeholder="Enter number of sensors")
    st.caption("Example: **150 units** of high-resolution sensors.")

    communication_inventory = st.number_input("📡 Communication Systems", min_value=0, placeholder="Enter number of communication systems")
    st.caption("Example: **100 units** of satellite communication modules.")

    solar_panels_inventory = st.number_input("🔋 Solar Panels", min_value=0, placeholder="Enter number of solar panels")
    st.caption("Example: **250 units** of solar panels for power generation.")

    # Propulsion Engines Inventory
    st.markdown("#### 🚀 Propulsion Engines Inventory Levels")

    ion_thrusters_inventory = st.number_input("🌀 Ion Thrusters", min_value=0, placeholder="Enter number of ion thrusters")
    st.caption("Example: **50 units** of ion propulsion engines.")
    
    chemical_rockets_inventory = st.number_input("🚀 Chemical Rockets", min_value=0, placeholder="Enter number of chemical rockets")
    st.caption("Example: **30 units** of chemical rocket engines.")

    # Lead Time for Components
    st.markdown("### 🕗 Lead Time for Components (in days)")
    sensors_lead_time = st.number_input("🔧 Sensors Lead Time", min_value=0, placeholder="Enter lead time for sensors in days")
    st.caption("Example: **20 days** for high-resolution sensors.")
    
    communication_lead_time = st.number_input("📡 Communication Systems Lead Time", min_value=0, placeholder="Enter lead time for communication systems in days")
    st.caption("Example: **15 days** for satellite communication modules.")
    
    solar_panels_lead_time = st.number_input("🔋 Solar Panels Lead Time", min_value=0, placeholder="Enter lead time for solar panels in days")
    st.caption("Example: **25 days** for solar panels.")
    
    ion_thrusters_lead_time = st.number_input("🌀 Ion Thrusters Lead Time", min_value=0, placeholder="Enter lead time for ion thrusters in days")
    st.caption("Example: **30 days** for ion propulsion engines.")
    
    chemical_rockets_lead_time = st.number_input("🚀 Chemical Rockets Lead Time", min_value=0, placeholder="Enter lead time for chemical rockets in days")
    st.caption("Example: **40 days** for chemical rocket engines.")

    # Transportation Modes
    transport = st.text_area("🚶 Transportation Modes", placeholder="List transportation methods and constraints")
    st.caption("Example: **Air freight, Sea shipping, Ground transport**.")

    # Help Button for Explanation
    if st.button("💡 Need Help?"):
        st.markdown("""
        **📦 Satellite Components Inventory Levels:** Input quantities for each critical component like sensors, communication systems, and solar panels.
        
        **🚀 Propulsion Engines Inventory Levels:** Input quantities for ion thrusters and chemical rockets.
        
        **🕗 Lead Time:** Time taken from order placement to delivery for each component.
        
        **🚶 Transportation Modes:** Methods of transporting goods, affecting delivery speed and cost.
        """)

    # Supply Chain AI Prompt
    supply_chain_optimizer_task = f"""
    Analyze inventory, lead time, and transportation inputs to optimize the supply chain.  

    ### **Supply Chain Summary**
    | Component                | Inventory Level | Lead Time (days) |
    |--------------------------|-----------------|-----------------|
    | Sensors                  | {sensors_inventory} units       | {sensors_lead_time} days       |
    | Communication Systems    | {communication_inventory} units | {communication_lead_time} days |
    | Solar Panels             | {solar_panels_inventory} units  | {solar_panels_lead_time} days  |
    | Ion Thrusters            | {ion_thrusters_inventory} units | {ion_thrusters_lead_time} days |
    | Chemical Rockets         | {chemical_rockets_inventory} units | {chemical_rockets_lead_time} days |

    ### **Optimized Supply Chain Breakdown**
    | Aspect            | Current Status       | Optimization Suggestion |
    |------------------|----------------------|--------------------------|
    | Inventory Levels | Detailed per component| Adjust stock to optimal levels |
    | Lead Time        | Varies by component   | Identify faster suppliers per item |
    | Transportation   | {transport}          | Combine modes for efficiency |

    ### **Optimization Strategy**
    - Balance inventory to reduce holding costs.
    - Streamline supplier processes to shorten lead times.
    - Optimize transportation routes to minimize delays and costs.
    """

    # Inefficiency Detection Prompt
    inefficiency_task = """
    Detect inefficiencies in inventory, lead time, and transportation, and suggest improvements.  
    Identify overstocking or understocking issues and suggest adjustments.  
    Detect delays in lead time and propose faster alternatives.  
    Analyze transport inefficiencies and recommend cost-effective routes.  

    ### **Inefficiency Detection & Fixes**
    | Issue              | Identified Cause                          | Suggested Fix |
    |-------------------|--------------------------------------|--------------|
    | Overstocking      | Excess inventory levels              | Adjust stock levels |
    | Long Lead Time    | Delayed supplier delivery            | Find faster suppliers |
    | Transport Delay   | Inefficient logistics                | Optimize shipping routes |
    """

    # Function to call AI Agents
    def generate_response(role, task, user_input):
        """ Calls Groq API for AI response """
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"You are a {role}. Your task is: {task}"},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=2000,
            )
            return response.choices[0].message.content if response.choices else "No response received."
        except Exception as e:
            return f"Error: {e}"

    # Session State for tracking results
    if "supply_chain_result" not in st.session_state:
        st.session_state.supply_chain_result = None
    if "inefficiency_result_supply" not in st.session_state:
        st.session_state.inefficiency_result_supply = None

    # Button to Execute AI Agents
    if st.button("🔍 Optimize Supply Chain"):
        st.subheader("✅ Smart Supply Chain Optimization:")
        st.session_state.supply_chain_result = generate_response(
            role="Smart Supply Chain Manager",
            task=supply_chain_optimizer_task,
            user_input="Optimize supply chain based on inventory, lead time, and transportation."
        )
        st.write(st.session_state.supply_chain_result)

    # Button for Inefficiency Detection
    if st.session_state.supply_chain_result:
        if st.button("⚠️ Check for Inefficiencies"):
            st.subheader("⚠️ Inefficiency Detection & Improvement Suggestions:")
            st.session_state.inefficiency_result_supply = generate_response(
                role="Supply Chain Inefficiency Detector",
                task=inefficiency_task,
                user_input="Analyze inefficiencies in inventory levels, lead time, and transportation."
            )

    # Display Inefficiency Result
    if st.session_state.inefficiency_result_supply:
        st.write(st.session_state.inefficiency_result_supply)

#--------------------------Communication Manager here-----------------------------------------------------
elif option == "Communication Manager":
    st.subheader("📡 AI Communication & Data Routing Manager")
    st.markdown("### Optimize Spacecraft Communication with Ground Control")

    # User Inputs for Communication Management
    signal_strength = st.text_input("📡 Signal Strength (in dB)", placeholder="Enter signal strength in dB")
    st.caption("Example: **50 dB** for strong signals, **30 dB** for weak signals.")

    latency = st.text_input("⏳ Latency (in ms)", placeholder="Enter communication latency")
    st.caption("Example: **200 ms** for normal delay, **500 ms** for high-latency issues.")

    message_priority = st.selectbox("🚨 Message Priority", ["Routine", "Critical", "Emergency"])
    st.caption("Critical messages are prioritized over routine ones.")

    error_rate = st.text_input("⚠️ Data Error Rate (%)", placeholder="Enter error rate in percentage")
    st.caption("Example: **1%** for minor errors, **10%** for severe data corruption.")

    # AI Agent Class
    class AIAgent:
        def __init__(self, role, task):
            self.role = role
            self.task = task

        def generate_response(self, input_text):
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": f"You are a {self.role}. Your task is: {self.task}"},
                        {"role": "user", "content": input_text}
                    ],
                    temperature=0.7,
                    max_tokens=2000,
                )
                return response.choices[0].message.content if response.choices else "No response received."
            except Exception as e:
                return f"Error: {e}"

    # Define AI Agents
    communication_optimizer = AIAgent(
        role="Communication Routing & Optimization Agent",
        task="""
        Analyze the given spacecraft communication parameters and provide **specific** optimizations tailored to the input data. The output should:
        
        - **Directly address weaknesses** in signal strength, latency, and error rate.
        - **Provide targeted, actionable recommendations** (avoid generic responses).
        - **Optimize message prioritization** based on urgency.
        - **Suggest the best routing strategy** with a **backup plan**.
        
        ### **Optimized Communication Summary**
        | Parameter         | Value |
        |------------------|-------|
        | Signal Strength  | {signal_input} dB |
        | Latency         | {latency_input} ms |
        | Priority        | {priority_input} |
        | Error Rate      | {error_rate_input} % |

        ### **Targeted Optimizations**
        - **Signal Strength**: {Specific fix based on signal_input}.
        - **Latency Reduction**: {Precise step to optimize latency_input}.
        - **Priority Handling**: {Message routing improvement based on priority_input}.
        - **Error Correction**: {Directly relevant solution for error_rate_input}.

        ### **Suggested Routing Strategy**
        - **Primary Ground Station**: Select {best option based on input values}.
        - **Backup Station**: {Fallback routing suggestion}.
        - **Error Handling**: {Recommended error mitigation strategy}.
        """
    )

    anomaly_detector = AIAgent(
        role="Communication Anomaly Detection Agent",
        task="""
        Detect anomalies in spacecraft-ground communication based on given parameters. The output should be **specific, compact, and focused on real issues**.

        - Identify **signal dropouts**, **high latency**, and **error trends**.
        - Provide **cause-based explanations** (no generic insights).
        - Recommend **direct, actionable fixes**.

        ### **Communication Anomaly Report**
        | Issue              | Identified Cause                          | Suggested Fix |
        |-------------------|--------------------------------------|--------------|
        | {Detected issue} | {Cause based on input data} | {Precise solution} |

        ### **Final Recommendations**
        - **Boost Signal Strength**: {If required, provide targeted fix}.
        - **Reduce Latency**: {Directly relevant action}.
        - **Enhance Error Handling**: {Specific correction method}.
        - **Monitor in Real-time**: {How to prevent future anomalies}.
        """
    )

    # Session state to persist results
    if "communication_result" not in st.session_state:
        st.session_state.communication_result = None
    if "anomaly_result" not in st.session_state:
        st.session_state.anomaly_result = None

    # Execute AI Agents
    if st.button("📡 Optimize Communication"):
        if signal_strength and latency and message_priority and error_rate:
            st.subheader("✅ Communication Optimization:")
            st.session_state.communication_result = communication_optimizer.generate_response(
                f"Optimize communication for a spacecraft with {signal_strength} dB signal strength, {latency} ms latency,"
                f" priority {message_priority}, and an error rate of {error_rate}%. Suggest best routing strategies."
            )
            st.write(st.session_state.communication_result)

    # Show Anomaly Detection Button Only After Optimization
    if st.session_state.communication_result:
        if st.button("⚠️ Check for Anomalies"):
            st.subheader("⚠️ Anomaly Detection:")
            st.session_state.anomaly_result = anomaly_detector.generate_response(
                f"Analyze communication anomalies for a spacecraft with {signal_strength} dB signal, {latency} ms latency,"
                f" priority {message_priority}, and error rate {error_rate}%. Identify issues and provide fixes."
            )

    # Display Anomaly Result Without Removing Optimization Result
    if st.session_state.anomaly_result:
        st.write(st.session_state.anomaly_result)

#---------------Mission Planner

# ---------------- Mission Planner ----------------
elif option == "Mission Planner":
    st.subheader("🚀 AI Space Mission Creator")

    st.markdown("### Plan Your Next Space Mission!")

    # Approximate Distances (in million km) from Earth
    planet_distances = {
        "Mars": 225,
        "Jupiter's Moon (Europa)": 628,
        "Saturn's Moon (Titan)": 1270,
        "Venus": 41,
        "Undiscovered Planet": random.randint(1500, 5000)  # Randomized for a new planet
    }

    # Average Spacecraft Speed 
    avg_speed_kmh = 58000  

    # User Inputs
    mission_name = st.text_input("🌌 Mission Name", placeholder="Enter your mission name")
    crew_size = st.number_input("👩‍🚀 Crew Size", min_value=1, max_value=10, value=3)
    include_ai_assistant = st.checkbox("🤖 Include AI Agents in the Mission", value=True)

    # Planet Selection
    planets = list(planet_distances.keys())
    destination = st.selectbox("🪐 Select Destination", planets)

    # Handling Undiscovered Planet Naming
    if destination == "Undiscovered Planet":
        planet_name = st.text_input("🔭 Name Your New Planet", placeholder="Enter a name for the undiscovered planet")
        if not planet_name:
            planet_name = "X-Planet-" + str(random.randint(100, 999))
    else:
        planet_name = destination

    # Calculate Travel Time (Assuming Constant Speed)
    distance_km = planet_distances[destination] * 1_000_000  
    travel_hours = distance_km / avg_speed_kmh
    travel_days = round(travel_hours / 24)
    mission_duration = random.randint(6, 36)  

    st.write(f"🚀 **Estimated Travel Time to {planet_name}:** {travel_days} days")
    st.write(f"⏳ **Mission Duration:** {mission_duration} months")

    # Define AI Agent Class
    class AIAgent:
        def __init__(self, role, task):
            self.role = role
            self.task = task

        def generate_response(self, input_text):
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": f"You are a {self.role}. Your task is: {self.task}"},
                        {"role": "user", "content": input_text}
                    ],
                    temperature=0.7,
                    max_tokens=2000,
                )
                return response.choices[0].message.content if response.choices else "No response received."
            except Exception as e:
                return f"Error: {e}"

    # AI Agents
    mission_planner = AIAgent(
        role="AI Space Mission Strategist",
        task=f"Generate a structured mission plan for {planet_name}. "
             "Present key details in tabular format with objectives, crew responsibilities, AI tasks, and discoveries."
    )

    risk_analyzer = AIAgent(
        role="AI Space Risk Assessor",
        task=f"Analyze potential risks for {planet_name} and present them in a structured table. "
             "Include environmental hazards, spacecraft challenges, and mitigation strategies."
    )

    resource_allocator = AIAgent(
        role="AI Space Logistics Manager",
        task=f"Allocate mission resources for {planet_name} in tabular format. "
             "Include fuel (liters), oxygen (tanks), water (bottles), food (kg), and backup supplies. "
             "Ensure additional emergency reserves for undiscovered planets."
    )

    # Generate Mission Plan
    if st.button("🚀 Generate Mission Plan"):
        if mission_name:
            st.subheader(f"📜 Mission Plan: {mission_name}")

            mission_details = mission_planner.generate_response(
                f"Create a structured mission plan for {mission_name} to {planet_name}. "
                "Use tabular format and include numeric values where applicable."
            )
            st.write(mission_details)

            st.subheader("⚠️ Risk Assessment:")
            risk_report = risk_analyzer.generate_response(
                f"Provide a structured risk assessment for {mission_name} to {planet_name}. "
                "Present threats and mitigation strategies in tabular format."
            )
            st.write(risk_report)

            st.subheader("🛰️ Resource Allocation & Backup Supplies:")
            resource_plan = resource_allocator.generate_response(
                f"Generate a structured table for mission resources to {planet_name}. "
                "Include numeric values for water, fuel, oxygen, food, and emergency reserves."
            )
            st.write(resource_plan)
        else:
            st.warning("Please enter a mission name before generating details.")


